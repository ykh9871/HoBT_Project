from django import forms
from .models import HobtDict, BIG_CATEGORY_CHOICES, APPEARANCE_DATE


class HobtDictForm(forms.ModelForm):
    class Meta:
        model = HobtDict
        fields = ['qid', 'answer', 'similar_answer', 'content', 'appearance_date', 'small_category', 'big_category', 'note']
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
        widgets = {
            'note': forms.Textarea(attrs={'rows': 4}),
            'qid': forms.NumberInput(attrs={'class': 'form-control'}),
            'big_category': forms.Select(attrs={'class': 'form-control'}),
            'appearance_date': forms.Select(attrs={'class': 'form-control'})
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
        self.fields['appearance_date'].choices = [('', '----------')] + APPEARANCE_DATE

    def as_row(self):
        return self._html_output(
            normal_row='<div class="row mb-3">'
                       '<div class="col-md-6">%s</div>'
                       '<div class="col-md-6">%s</div></div>',
            error_row='%s',
            row_ender='</div>',
            help_text_html=' <span class="form-text text-muted">%s</span>',
            errors_on_separate_row=True)
