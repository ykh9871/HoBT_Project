from django import forms
from .models import HobtDict


class HobtDictForm(forms.ModelForm):
    class Meta:
        model = HobtDict
        fields = ['qid', 'answer', 'similar_answer', 'content', 'appearance_date', 'small_category', 'big_category', 'note']
        labels = {
            'qid': '문제 번호',
            'answer': '정답',
            'similar_answer': '유사 답안',
            'content': '문제 내용',
            'appearance_date': '출제 연도 예/2020년 1회 실기',
            'small_category': '소 분류',
            'big_category': '대 분류',
            'note': '비고'
        }