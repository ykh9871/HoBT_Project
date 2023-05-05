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


# 정보처리기사 문제만 보여주는 뷰 함수
def cs_dict(request):
    q = request.GET.get('q', '')  # 검색어
    cs_dict_list = HobtDict.objects.filter(subject='정보처리기사').order_by('-qid')

    if q:
        cs_dict_list = cs_dict_list.filter(
            Q(answer__icontains=q) | Q(similar_answer__icontains=q) | Q(content__icontains=q) | Q(qid__icontains=q)
            | Q(small_category__icontains=q) | Q(big_category__icontains=q) | Q(appearance_date__icontains=q)
        ).distinct()

    paginator = Paginator(cs_dict_list, 10)
    page = request.GET.get('page', 1)
    cs_dicts = paginator.get_page(page)

    start_index = max(1, cs_dicts.number - 5)
    end_index = min(start_index + 10, cs_dicts.paginator.num_pages + 1)
    page_range = range(start_index, end_index)

    context = {'cs_dicts': cs_dicts, 'page': page, 'q': q, 'page_range': page_range}
    return render(request, 'hobt_dict/CS_dict.html', context)


def cs_search(request):
    """
    문제 검색 기능
    """
    q = request.GET.get('q', '')  # 검색어
    page = request.GET.get('page', '1')  # 페이지

    cs_dict_list = HobtDict.objects.filter(subject='정보처리기사').order_by('-qid')
    if q:
        cs_dict_list = cs_dict_list.filter(
            Q(answer__icontains=q) | Q(similar_answer__icontains=q) | Q(content__icontains=q)| Q(qid__icontains=q)
            | Q(small_category__icontains=q)| Q(big_category__icontains=q)| Q(appearance_date__icontains=q) |
            Q(subject__icontains=q)
        ).distinct()

    paginator = Paginator(cs_dict_list, 10)
    cs_dicts = paginator.get_page(page)

    start_index = max(1, cs_dicts.number - 5)
    end_index = min(start_index + 10, cs_dicts.paginator.num_pages + 1)
    page_range = range(start_index, end_index)

    context = {'cs_dicts': cs_dicts, 'page': page, 'q': q, 'page_range': page_range}
    return render(request, 'hobt_dict/CS_dict.html', context)