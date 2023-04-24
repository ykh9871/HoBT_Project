from django.urls import path
from . import views

app_name = 'hobt'

urlpatterns = [
    # localhost:8000/hobt 주소의 루트를 의미함
    path('', views.index, name='index'),
    
    # 게시글 제목의 a 태그 href 속성에 해당하는 동적 URL 매핑
    path('<int:question_id>/', views.detail, name='detail'),
    
    # 답변 등록에 대한 URL 매핑
    path('answer/create/<int:question_id>/', views.answer_create, name="answer_create"),

    # 질문 등록에 대한 URL 매핑
    path("question/create/", views.question_create, name='question_create'),

    # 게시판 페이지에 대한 URL 매핑
    path('question/', views.question, name='question'),
    # 질문 수정에 대한 URL 매핑
    path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'),
    # 질문 삭제에 대한 URL 매핑
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),
    # 답변 수정에 대한 URL 매핑
    path('answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'),
    # 답변 삭제에 대한 URL 매핑
    path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),
    # 질문 추천 URL 매핑
    path('question/vote/<int:question_id>/', views.question_vote, name='question_vote'),
    # 답변 추천 URL 매핑
    path('answer/vote/<int:answer_id>/', views.answer_vote, name='answer_vote'),
]