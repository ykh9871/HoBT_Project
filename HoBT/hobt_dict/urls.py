from django.urls import path
from . import views

app_name = 'hobt_dict'
urlpatterns = [
    path('', views.hobt_dict, name='hobt_dict'), # 문제 사전 게시판 메인 페이지
    # path('create/', views.HobtDictCreateView.as_view(), name='hobt_dict_create'), # 문제 등록 현재는 사용하지 않는기능
    path('<int:pk>/modify/', views.hobt_dict_modify, name='hobt_dict_modify'), # 문제 수정
    path('<int:pk>/delete/', views.hobt_dict_delete, name='hobt_dict_delete'), # 문제 삭제
    path('like/<int:pk>/\\Z', views.hobt_dict_like, name='hobt_dict_like'), # 문제 추천
    path('<int:pk>/', views.hobt_dict_detail, name='hobt_dict_detail'), # 문제 상세보기
    path('search/', views.search, name='search'), # 검색기능
    path('add_problem/', views.add_problem, name='add_problem'), # 사용자가 문제를 추가
    path('problem_list/', views.show_problems, name='problem_list'), # 사용자 및 관리자가 추가한 문제 검토 리스트
    path('add_selected_problems/', views.add_selected_problems, name='add_selected_problems'),
    path('delete_selected_problems/', views.delete_selected_problems, name='delete_selected_problems'), # 체크박스 선택 항목 삭제
]