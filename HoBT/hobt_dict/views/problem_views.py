from django.urls import reverse_lazy
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
import json
from django.contrib.auth.models import User
from ..models import Problem
from ..forms import ProblemForm


def add_problem(request):
    if request.method == 'POST':
        form = ProblemForm(request.POST)
        problem_user = request.user  # 로그인 한 사람의 username
        same_user = User.objects.get(username=problem_user).id
        if form.is_valid():
            problem = form.save(commit=False)
            problem.author_id = same_user
            problem.save()
            return redirect('hobt_dict:problem_list')
    else:
        form = ProblemForm()
    return render(request, 'hobt_dict/add_problem.html', {'form': form})


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
    return redirect(reverse_lazy('hobt_dict:hobt_dict'))


def delete_selected_problems(request):
    if request.method == 'POST':
        selected_problem_ids = json.loads(request.body)['selected_problem_ids']  # 요청 데이터에서 선택한 문제들의 ID 목록 가져오기
        problems_to_delete = Problem.objects.filter(qid__in=selected_problem_ids)  # 선택한 문제들 필터링
        problems_to_delete.delete()  # 선택한 문제들 삭제하기

        return JsonResponse({'success': True})  # 성공적으로 삭제됐음을 응답으로 보내기

    return JsonResponse({'success': False})  # POST 요청이 아니면 실패로 응답하기
