from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from .forms import UserForm


@login_required(login_url='common:login')
def withdrawal(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        if request.user.check_password(password):  # 비밀번호 검증
            request.user.delete()  # 현재 로그인한 사용자를 삭제
            logout(request)  # 로그아웃
            return redirect('hobt:index')
        else:
            error_msg = '비밀번호가 일치하지 않습니다.'
            return render(request, 'common/withdrawal.html', {'error_msg': error_msg})
    else:
        return render(request, 'common/withdrawal.html')


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")  # 회원가입이 완료되면 index 페이지로 이동
    else:  # GET 요청일 때
        form = UserForm()
    return render(request, "common/signup.html", {"form": form})