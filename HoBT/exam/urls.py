from django.urls import path
from .views import add_problem
from . import views

app_name = 'exam'

urlpatterns = [
    path('add_problem/', views.add_problem, name='add_problem'),
    path('problem_list/', views.show_problems, name='problem_list'),
]