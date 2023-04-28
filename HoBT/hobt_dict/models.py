from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

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


class HobtDict(models.Model):
    """
    문제 사전 모델
    """
    qid = models.AutoField(verbose_name='문제 번호', primary_key=True)
    answer = models.CharField(verbose_name='정답', max_length=255)
    similar_answer = models.CharField(verbose_name='유사 답안', max_length=255, blank=True)
    content = models.TextField(verbose_name='문제 내용')
    appearance_date = models.CharField(
        verbose_name='출제 유형',
        max_length=255,
        choices=APPEARANCE_DATE_CHOICES,  # choices 속성에 정의한 카테고리 선택 사항 할당
        blank=True
    )
    small_category = models.CharField(verbose_name='소 분류', max_length=255, blank=True)
    big_category = models.CharField(
        verbose_name='대 분류',
        max_length=255,
        choices=BIG_CATEGORY_CHOICES,  # choices 속성에 정의한 카테고리 선택 사항 할당
        blank=True
    )
    note = models.TextField(verbose_name='비고', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='등록일')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정일')
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='author_hobtdict')
    like = models.ManyToManyField(User, related_name='liker_hobtdict')

    def get_absolute_url(self):
        return reverse('hobt_dict:hobt_dict_detail', args=[str(self.qid)])


class Problem(models.Model):
    qid = models.AutoField(verbose_name='문제 번호', primary_key=True)
    answer = models.CharField(verbose_name='정답', max_length=255)
    similar_answer = models.CharField(verbose_name='유사 답안', max_length=255, blank=True)
    content = models.TextField(verbose_name='문제 내용')
    appearance_date = models.CharField(
        verbose_name='출제 유형',
        max_length=255,
        choices=APPEARANCE_DATE_CHOICES,  # choices 속성에 정의한 카테고리 선택 사항 할당
        blank=True
    )
    small_category = models.CharField(verbose_name='소 분류', max_length=255, blank=True)
    big_category = models.CharField(
        verbose_name='대 분류',
        max_length=255,
        choices=BIG_CATEGORY_CHOICES,  # choices 속성에 정의한 카테고리 선택 사항 할당
        blank=True
    )
    note = models.TextField(verbose_name='비고', blank=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        db_table = 'exam_problem'