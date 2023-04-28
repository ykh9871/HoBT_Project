from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.contrib.admin.views.decorators import staff_member_required

from ..models import HobtDict
from ..forms import HobtDictForm


def hobt_dict(request):
    """
    문제 사전 게시판 메인 페이지
    """
    # 페이지네이션 기능 추가
    q = request.GET.get('q', '')  # 검색어
    page = request.GET.get('page', '1')  # 페이지

    hobt_dict_list = HobtDict.objects.order_by('-qid')
    if q:
        hobt_dict_list = hobt_dict_list.filter(
            Q(answer__icontains=q) | Q(similar_answer__icontains=q) | Q(content__icontains=q) | Q(qid__icontains=q)
            | Q(small_category__icontains=q) | Q(big_category__icontains=q) | Q(appearance_date__icontains=q)
        ).distinct()

    paginator = Paginator(hobt_dict_list, 10)
    hobt_dicts = paginator.get_page(page)

    start_index = max(1, hobt_dicts.number - 5)
    end_index = min(start_index + 10, hobt_dicts.paginator.num_pages + 1)
    page_range = range(start_index, end_index)

    context = {'hobt_dicts': hobt_dicts, 'page': page, 'q': q, 'page_range': page_range}
    return render(request, 'hobt_dict/hobt_dict.html', context)

# 현재는 사용하지 않는기능
# class HobtDictCreateView(View):
#     """
#     문제 등록
#     """
#     def get(self, request):
#         form = HobtDictForm()
#         return render(request, 'hobt_dict/hobt_dict_form.html', {'form': form})
#
#     def post(self, request):
#         form = HobtDictForm(request.POST)
#         if form.is_valid():
#             hobt_dict = form.save(commit=False)
#             hobt_dict.author = request.user
#             hobt_dict.save()
#             messages.success(request, '문제가 등록되었습니다.')
#             return redirect(hobt_dict)
#         return render(request, 'hobt_dict/hobt_dict_form.html', {'form': form})


@staff_member_required
def hobt_dict_modify(request, pk):
    """
    문제 수정
    """
    hobt_dict = get_object_or_404(HobtDict, pk=pk)
    # if request.user != hobt_dict.author:
    #     messages.error(request, '수정권한이 없습니다')
    #     return redirect('hobt_dict:hobt_dict_detail', pk=hobt_dict.pk)
    # 접근 자체를 관리자만 접근 할 수 있도록 작성해서 주석처리
    if request.method == 'POST':
        form = HobtDictForm(request.POST, instance=hobt_dict)
        if form.is_valid():
            hobt_dict = form.save(commit=False)
            hobt_dict.author = request.user
            hobt_dict.save()
            form.save_m2m()  # ManyToManyField를 저장하는 데 필요
            messages.success(request, '문제가 수정되었습니다')
            return redirect(hobt_dict)
    else:
        form = HobtDictForm(instance=hobt_dict)
    context = {
        'form': form,
        'qid': hobt_dict.qid,
    }
    return render(request, 'hobt_dict/hobt_dict_modify.html', context)


@login_required(login_url='common:login')
def hobt_dict_delete(request, pk):
    """
    문제 삭제
    """
    hobt_dict = get_object_or_404(HobtDict, pk=pk)
    if request.user != hobt_dict.author:
        messages.error(request, '삭제권한이 없습니다')
    else:
        hobt_dict.delete()
        messages.success(request, '문제가 삭제되었습니다.')
        return redirect('hobt_dict:hobt_dict')


@login_required(login_url='common:login')
@require_POST
def hobt_dict_like(request, pk):
    """
    문제 추천
    """
    hobt_dict = get_object_or_404(HobtDict, pk=pk)
    if hobt_dict.like.filter(id=request.user.id).exists():
        # 이미 추천한 경우
        hobt_dict.like.remove(request.user)
        message = '추천을 취소했습니다.'
    else:
        # 추천하지 않은 경우
        hobt_dict.like.add(request.user)
        message = '문제를 추천했습니다.'
    context = {'like_count': hobt_dict.like.count(), 'message': message}
    return JsonResponse(context)


def hobt_dict_detail(request, pk):
    hobt_dict = get_object_or_404(HobtDict, pk=pk)
    context = {'hobt_dict': hobt_dict}
    return render(request, 'hobt_dict/detail.html', context)


def search(request):
    """
    문제 검색 기능
    """
    q = request.GET.get('q', '')  # 검색어
    page = request.GET.get('page', '1')  # 페이지

    hobt_dict_list = HobtDict.objects.order_by('-qid')
    if q:
        hobt_dict_list = hobt_dict_list.filter(
            Q(answer__icontains=q) | Q(similar_answer__icontains=q) | Q(content__icontains=q)| Q(qid__icontains=q)
            | Q(small_category__icontains=q)| Q(big_category__icontains=q)| Q(appearance_date__icontains=q)
        ).distinct()

    paginator = Paginator(hobt_dict_list, 10)
    hobt_dicts = paginator.get_page(page)

    start_index = max(1, hobt_dicts.number - 5)
    end_index = min(start_index + 10, hobt_dicts.paginator.num_pages + 1)
    page_range = range(start_index, end_index)

    context = {'hobt_dicts': hobt_dicts, 'page': page, 'q': q, 'page_range': page_range}
    return render(request, 'hobt_dict/hobt_dict.html', context)