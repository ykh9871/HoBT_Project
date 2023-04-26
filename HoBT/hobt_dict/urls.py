from django.urls import path
from . import views

app_name = 'hobt_dict'
urlpatterns = [
    path('', views.hobt_dict, name='hobt_dict'), # 문제 사전 게시판 메인 페이지
    path('create/', views.HobtDictCreateView.as_view(), name='hobt_dict_create'), # 문제 등록
    path('<int:pk>/modify/', views.hobt_dict_modify, name='hobt_dict_modify'), # 문제 수정
    path('<int:pk>/delete/', views.hobt_dict_delete, name='hobt_dict_delete'), # 문제 삭제
    path('like/<int:pk>/\\Z', views.hobt_dict_like, name='hobt_dict_like'), # 문제 추천
    path('<int:pk>/', views.hobt_dict_detail, name='hobt_dict_detail'), # 문제 상세보기
    path('search/', views.search, name='search') # 검색기능
]