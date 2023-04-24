from django.db import models
from django import forms


STATUS_CHOICES = (
    (1, '사용 가능'),
    (2, '사용 불가'),
)


class Problem(models.Model):
    qid = models.IntegerField(primary_key=True)
    answer = models.CharField(max_length=100)
    similar_answer = models.TextField(blank=True)
    content = models.TextField()
    appearance_date = models.DateField()
    small_category = models.CharField(max_length=100)
    big_category = models.CharField(max_length=100)
    note = models.TextField(blank=True)

    def __str__(self):
        return f'Problem {self.qid}'

    class Meta:
        ordering = ['qid']
        