from django.urls import path
from . import views

app_name = 'exam'

urlpatterns = [
    path('exam_judge/', views.exam_judge, name='exam_judge'),
    path('exam/', views.exam, name='exam')
]
