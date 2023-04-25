from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User


class HobtDict(models.Model):
    """
    문제 사전 모델
    """
    qid = models.AutoField(verbose_name='문제 번호', primary_key=True)
    answer = models.CharField(verbose_name='정답', max_length=255)
    similar_answer = models.CharField(verbose_name='유사 답안', max_length=255, blank=True)
    content = models.TextField(verbose_name='문제 내용')
    appearance_date = models.CharField(verbose_name='출제 연도 예/2020년 1회 실기', max_length=255, blank=True)
    small_category = models.CharField(verbose_name='소 분류', max_length=255, blank=True)
    big_category = models.CharField(verbose_name='대 분류', max_length=255, blank=True)
    note = models.TextField(verbose_name='비고', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='등록일')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정일')
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    like = models.ManyToManyField(User, related_name='liked_hobt_dicts')

    def __str__(self):
        return self.content[:50]

    def get_absolute_url(self):
        return reverse('hobt_dict:hobt_dict_detail', args=[str(self.qid)])
