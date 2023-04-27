from ..models import Problem


from django.urls import reverse_lazy
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, get_object_or_404


def add_problem(request):
    if request.method == 'POST':
        qid = request.POST.get('qid')
        answer = request.POST.get('answer')
        similar_answer = request.POST.get('similar_answer')
        content = request.POST.get('content')
        appearance_date = request.POST.get('appearance_date')
        small_category = request.POST.get('small_category')
        big_category = request.POST.get('big_category')
        note = request.POST.get('note')
        problem = Problem(
            qid=qid,
            answer=answer,
            similar_answer=similar_answer,
            content=content,
            appearance_date=appearance_date,
            small_category=small_category,
            big_category=big_category,
            note=note
        )
        problem.save()
        return redirect(reverse_lazy('exam:problem_list'))
    return render(request, 'hobt_dict/add_problem.html')


def show_problems(request):
    problems = Problem.objects.all()
    return render(request, 'hobt_dict/problem_list.html', {'problems': problems})


@staff_member_required
@user_passes_test(lambda u: u.is_superuser)
def add_selected_problems(request):
    if request.method == 'POST':
        selected_problems = request.POST.getlist('selected_problems')
        for qid in selected_problems:
            problem = Problem.objects.get(qid=qid)
            # 문제의 정답을 사용자가 입력한 값으로 바꿈
            problem.answer = request.POST.get('answer' + qid)
            problem.save()
        return redirect(reverse_lazy('hobt_dict:problem_list'))
    return redirect(reverse_lazy('hobt:index'))