from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'common'

urlpatterns = [
    # Django에서 지원하는 views 라이브러리를 활용 (로그인, 로그아웃, 비밀번호 찾기&초기화 등)
    # pybo.urls에서 연결되는 views.py 파일의 함수를 만들 필요가 없음(Django가 알아서 다 처리)
    path('login/', auth_views.LoginView.as_view(template_name="common/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('signup/', views.signup, name="signup"),
    path('withdrawal/', views.withdrawal, name='withdrawal'),
]