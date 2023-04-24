from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    return render(request, 'hobt/index.html')


def question(request):
    page = request.GET.get("page", "1")  # 페이지의 번호를 가져옴 (그런데 첫 페이지는 1의 기본값 설정)
    question_list = Question.objects.order_by('-create_date')
    paginator = Paginator(question_list, 10)  # 페이지당 10개로 게시글을 제한
    page_obj = paginator.get_page(page)  # 전체 데이터에서 요청한 페이지에 관한 게시글만 추출
    context = {'question_list': page_obj}
    return render(request, 'hobt/question_list.html', context)
    # Templates 경로는 C:/projects/mysite/templates
    # 'hobt/question_list.html' -> 'hobt/' 경로를 직접 생성이 필요


def detail(request, question_id):
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'hobt/question_detail.html', context)


def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect("hobt:detail", question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'hobt/question_detail.html', context)


def question_create(request):
    if request.method == "POST":  # Post 요청일때는 입력한 값들을 전달받아 DB에 저장
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect("hobt:question")
    else:  # Get 요청일때는 단순히 질문등록 페이지 요청
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'hobt/question_form.html', context)
