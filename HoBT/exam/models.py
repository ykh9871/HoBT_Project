from django.db import models


class Problem(models.Model):
    qid = models.IntegerField(primary_key=True)
    answer = models.TextField()
    similar_answer = models.TextField()
    content = models.TextField()
    appearance_date = models.TextField()
    small_category = models.TextField()
    big_category = models.TextField()
    note = models.TextField()

    class Meta:
        db_table = 'exam_problem'


class Hobt1(models.Model):
    qid = models.IntegerField(primary_key=True)
    answer = models.TextField()
    similar_answer = models.TextField()
    content = models.TextField()
    appearance_date = models.TextField()
    small_category = models.TextField()
    big_category = models.TextField()
    note = models.TextField()

    class Meta:
        db_table = 'hobt_1'
        ordering = ['qid']
