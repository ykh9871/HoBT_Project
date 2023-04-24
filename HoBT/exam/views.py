from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Problem
from django.shortcuts import redirect


@staff_member_required
@user_passes_test(lambda u: u.is_superuser)
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
        problem = Problem(qid=qid, answer=answer, similar_answer=similar_answer, content=content, appearance_date=appearance_date, small_category=small_category, big_category=big_category, note=note)
        problem.save()
        return redirect(reverse_lazy('exam:problem_list'))
    return render(request, 'exam/add_problem.html')


def show_problems(request):
    problems = Problem.objects.all()
    return render(request, 'exam/problem_list.html', {'problems': problems})