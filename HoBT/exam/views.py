from django.shortcuts import render, redirect, get_object_or_404
from .models import Hobt1



def exam(request):
    hobt_1_list = Hobt1.objects.all()
    return render(request, 'exam/exam.html', {'hobt_1': hobt_1_list})


def exam_judge(request):
    problem_id = request.GET.get('problem_id', '')
    problem = Hobt1.objects.get(qid=problem_id)
    first_answer = request.GET.get('answer', '')
    answer = problem.answer
    similar_answer = problem.similar_answer
    is_correct = first_answer.strip() == answer.strip()
    context = {
        'problem_id': problem_id,
        'first_answer': first_answer,
        'answer': answer,
        'similar_answer': similar_answer,
        'is_correct': is_correct,
    }
    return render(request, 'exam/exam_judge.html', context)
