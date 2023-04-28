import pandas as pd
from django.shortcuts import render, redirect, get_object_or_404
from .models import Hobt1
from hobt_dict.models import HobtDict
from .utils import wrap_text
from django.http import HttpResponse

def exam(request):
    hobt_1_list = Hobt1.objects.all()
    # for problem in hobt_1_list:
    #     problem.content = problem.content.replace('.', '.<br>').replace('?', '?<br>')
    # 세션에서 data_list를 가져옴
    data_list = request.session.get('data_list', [])
    return render(request, 'exam/exam.html', {'data_list': data_list})


def exam_judge(request):
    problem_id = request.GET.get('problem_id', '')
    problem = HobtDict.objects.get(qid=problem_id)
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

def exam_result(request):
    return render(request, 'exam/exam_result.html')


def exam_select(request):

    qs = HobtDict.objects.all().values()
    data = pd.DataFrame(qs)
    random_data = data.sample(n=20, replace=False).reset_index(drop=True)

    # 데이터 프레임을 딕셔너리 목록으로 변환
    data_list = random_data.to_dict('records')

    for item in data_list:
        for key, value in item.items():
            if isinstance(value, pd.Timestamp):
                # Timestamp 객체를 문자열로 변환
                item[key] = value.strftime('%Y-%m-%d %H:%M:%S')
            elif pd.isna(value):
                # NaTType 객체를 빈 문자열로 변환
                item[key] = ''



    # data_list를 세션 변수로 저장
    request.session['data_list'] = data_list

    context = {'data_list': data_list}
    return render(request, 'exam/exam_select.html', context)


