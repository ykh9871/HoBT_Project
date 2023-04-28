from django.urls import reverse_lazy
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
import json
from django.contrib.auth.models import User
from ..models import Problem, HobtDict
from ..forms import ProblemForm
from django.utils import timezone
from django.db.models import Max


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
def add_selected_problems(request):
    if request.method == 'POST':
        selected_problem_qids = request.POST.getlist('selected_problem_qids')
        exam_problems = Problem.objects.filter(qid__in=selected_problem_qids)
        max_qid = HobtDict.objects.aggregate(Max('exam_problem__qid'))['exam_problem__qid__max'] or 0  # 최대값이 없을 경우 0으로 초기화
        for exam_problem in exam_problems:
            # 새로운 HobtDict 레코드 생성
            hobt_dict = HobtDict.objects.create(
                exam_problem=exam_problem,
                qid=max_qid + exam_problem.qid,
                created_at=timezone.now(),
                updated_at=None,
                author_id=request.user.id
            )

        return HttpResponse('문제가 성공적으로 추가되었습니다.')


def delete_selected_problems(request):
    if request.method == 'POST':
        selected_problem_qids = json.loads(request.body)['selected_problem_qids']  # 요청 데이터에서 선택한 문제들의 QID 목록 가져오기
        problems_to_delete = Problem.objects.filter(qid__in=selected_problem_qids)  # 선택한 문제들 필터링
        problems_to_delete.delete()  # 선택한 문제들 삭제하기

        return JsonResponse({'success': True})  # 성공적으로 삭제됐음을 응답으로 보내기

    return JsonResponse({'success': False})  # POST 요청이 아니면 실패로 응답하기
