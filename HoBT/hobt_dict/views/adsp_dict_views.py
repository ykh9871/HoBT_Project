from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from ..models import HobtDict


# ADsP 문제만 보여주는 뷰 함수
def adsp_dict(request):
    q = request.GET.get('q', '')  # 검색어
    adsp_dict_list = HobtDict.objects.filter(subject='ADsP').order_by('-qid')

    if q:
        adsp_dict_list = adsp_dict_list.filter(
            Q(answer__icontains=q) | Q(similar_answer__icontains=q) | Q(content__icontains=q) | Q(qid__icontains=q)
            | Q(small_category__icontains=q) | Q(big_category__icontains=q) | Q(appearance_date__icontains=q)
        ).distinct()

    paginator = Paginator(adsp_dict_list, 10)
    page = request.GET.get('page', 1)
    adsp_dicts = paginator.get_page(page)

    start_index = max(1, adsp_dicts.number - 5)
    end_index = min(start_index + 10, adsp_dicts.paginator.num_pages + 1)
    page_range = range(start_index, end_index)

    context = {'adsp_dicts': adsp_dicts, 'page': page, 'q': q, 'page_range': page_range}
    return render(request, 'hobt_dict/ADsP_dict.html', context)


def adsp_search(request):
    """
    문제 검색 기능
    """
    q = request.GET.get('q', '')  # 검색어
    page = request.GET.get('page', '1')  # 페이지

    adsp_dict_list = HobtDict.objects.filter(subject='ADsP').order_by('-qid')
    if q:
        adsp_dict_list = adsp_dict_list.filter(
            Q(answer__icontains=q) | Q(similar_answer__icontains=q) | Q(content__icontains=q)| Q(qid__icontains=q)
            | Q(small_category__icontains=q)| Q(big_category__icontains=q)| Q(appearance_date__icontains=q) |
            Q(subject__icontains=q)
        ).distinct()

    paginator = Paginator(adsp_dict_list, 10)
    adsp_dicts = paginator.get_page(page)

    start_index = max(1, adsp_dicts.number - 5)
    end_index = min(start_index + 10, adsp_dicts.paginator.num_pages + 1)
    page_range = range(start_index, end_index)

    context = {'adsp_dicts': adsp_dicts, 'page': page, 'q': q, 'page_range': page_range}
    return render(request, 'hobt_dict/ADsP_dict.html', context)