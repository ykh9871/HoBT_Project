from django.urls import path
from . import views

app_name = 'exam'

urlpatterns = [
    path('add_problem/', views.add_problem, name='add_problem'),
    path('problem_list/', views.show_problems, name='problem_list'),
    path('add_selected_problems/', views.add_selected_problems, name='add_selected_problems'),
    path('exam_judge/', views.exam_judge, name='exam_judge'),
    path('exam/', views.exam, name='exam')
]
