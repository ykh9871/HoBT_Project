from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# Models의 Model이란 클래스 상속
class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=200) # models에서 문자열 필드(200바이트까지 제한)
    content = models.TextField() # 문자열 제한이 없는 데이터 타입
    create_date = models.DateTimeField() # 날짜와 시간
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question')  # 추천인 추가

    def __str__(self):
        return self.subject


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete= models.CASCADE) # Question을 외래키로, 삭제시 참조되는 모든걸 삭제
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')