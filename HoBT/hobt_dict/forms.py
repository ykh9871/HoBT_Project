from django import forms
from .models import Problem, HobtDict, BIG_CATEGORY_CHOICES, APPEARANCE_DATE_CHOICES, SUBJECT_CHOICES


class HobtDictForm(forms.ModelForm):
    class Meta:
        model = HobtDict
        fields = ['qid', 'answer', 'similar_answer', 'content', 'appearance_date', 'small_category', 'big_category', 'note', 'subject']
        labels = {
            'qid': '문제 번호',
            'answer': '정답',
            'similar_answer': '유사 답안',
            'content': '문제 내용',
            'appearance_date': '출제 유형',
            'small_category': '소분류',
            'big_category': '대분류',
            'note': '비고',
            'subject': '과목'
        }
        widgets = {
            'note': forms.Textarea(attrs={'rows': 4}),
            'qid': forms.NumberInput(attrs={'class': 'form-control'}),
            'big_category': forms.Select(attrs={'class': 'form-control'}),
            'appearance_date': forms.Select(attrs={'class': 'form-control'}),
            'subject': forms.Select(attrs={'class': 'form-control'}),
        }
        error_css_class = 'is-invalid'
        required_css_class = 'required'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add bootstrap classes to the form fields
        for field in self.fields.values():
            if isinstance(field.widget, forms.TextInput):
                field.widget.attrs.update({'class': 'form-control'})
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({'class': 'form-control'})
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs.update({'class': 'form-select'})

        # Set form labels as bootstrap sr-only class
        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = field.label
            field.widget.attrs['aria-label'] = field.label
            field.label = ''
        self.fields['big_category'].choices = [('', '----------')] + BIG_CATEGORY_CHOICES
        self.fields['appearance_date'].choices = [('', '----------')] + APPEARANCE_DATE_CHOICES
        self.fields['subject'].choices = [('', '----------')] + SUBJECT_CHOICES

    def as_row(self):
        return self._html_output(
            normal_row='<div class="row mb-3">'
                       '<div class="col-md-6">%s</div>'
                       '<div class="col-md-6">%s</div></div>',
            error_row='%s',
            row_ender='</div>',
            help_text_html=' <span class="form-text text-muted">%s</span>',
            errors_on_separate_row=True)


# forms.py
class ProblemForm(forms.ModelForm):
    BIG_CATEGORY_CHOICES = [
        ('SQL 응용', 'SQL 응용'),
        ('데이터 입출력 구현', '데이터 입출력 구현'),
        ('서버 프로그램 구현', '서버 프로그램 구현'),
        ('소프트웨어 개발 보안 구축', '소프트웨어 개발 보안 구축'),
        ('애플리케이션 테스트 관리', '애플리케이션 테스트 관리'),
        ('요구사항 확인', '요구사항 확인'),
        ('응용 SW 기초 기술 활용', '응용 SW 기초 기술 활용'),
        ('인터페이스 구현', '인터페이스 구현'),
        ('정보처리 실무 일반(기타)', '정보처리 실무 일반(기타)'),
        ('제품 소프트웨어 패키징', '제품 소프트웨어 패키징'),
        ('통합 구현', '통합 구현'),
        ('프로그래밍 언어 활용', '프로그래밍 언어 활용'),
        ('화면 설계', '화면 설계'),
        # 추가 카테고리를 필요에 따라 추가하세요.
    ]

    APPEARANCE_DATE_CHOICES = [
        ('2020년 1회 실기', '2020년 1회 실기'),
        ('2020년 2회 실기', '2020년 2회 실기'),
        ('2020년 3회 실기', '2020년 3회 실기'),
        ('2020년 4회 실기', '2020년 4회 실기'),
        ('2021년 1회 실기', '2021년 1회 실기'),
        ('2021년 2회 실기', '2021년 2회 실기'),
        ('2021년 3회 실기', '2021년 3회 실기'),
        ('2022년 1회 실기', '2022년 1회 실기'),
        ('2022년 2회 실기', '2022년 2회 실기'),
        ('기출 예상 문제', '기출 예상 문제'),
        ('2020년 1회 필기', '2020년 1회 필기'),
        ('2020년 2회 필기', '2020년 2회 필기'),
        ('2020년 3회 필기', '2020년 3회 필기'),
        ('2021년 1회 필기', '2021년 1회 필기'),
        ('2021년 2회 필기', '2021년 2회 필기'),
        ('2021년 3회 필기', '2021년 3회 필기'),
        ('2022년 1회 필기', '2022년 1회 필기'),
        ('2022년 2회 필기', '2022년 2회 필기'),
        # 추가 카테고리를 필요에 따라 추가하세요.
    ]
    big_category = forms.ChoiceField(choices=BIG_CATEGORY_CHOICES)
    appearance_date = forms.ChoiceField(choices=APPEARANCE_DATE_CHOICES)
    class Meta:
        model = Problem
        fields = ['qid', 'answer', 'similar_answer', 'content', 'appearance_date', 'small_category', 'big_category',
                  'note']
        labels = {
            'qid': '문제 번호',
            'answer': '정답',
            'similar_answer': '유사 답안',
            'content': '문제 내용',
            'appearance_date': '출제 유형',
            'small_category': '소분류',
            'big_category': '대분류',
            'note': '비고'
        }
