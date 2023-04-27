# Generated by Django 4.2 on 2023-04-27 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hobt_dict', '0003_alter_hobtdict_big_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('qid', models.IntegerField(primary_key=True, serialize=False)),
                ('answer', models.TextField()),
                ('similar_answer', models.TextField()),
                ('content', models.TextField()),
                ('appearance_date', models.TextField()),
                ('small_category', models.TextField()),
                ('big_category', models.TextField()),
                ('note', models.TextField()),
            ],
            options={
                'db_table': 'exam_problem',
            },
        ),
        migrations.AlterField(
            model_name='hobtdict',
            name='appearance_date',
            field=models.CharField(blank=True, choices=[('2020년 1회 실기', '2020년 1회 실기'), ('2020년 2회 실기', '2020년 2회 실기'), ('2020년 3회 실기', '2020년 3회 실기'), ('2020년 4회 실기', '2020년 4회 실기'), ('2021년 1회 실기', '2021년 1회 실기'), ('2021년 2회 실기', '2021년 2회 실기'), ('2021년 3회 실기', '2021년 3회 실기'), ('2022년 1회 실기', '2022년 1회 실기'), ('2022년 2회 실기', '2022년 2회 실기'), ('기출 예상 문제', '기출 예상 문제'), ('2020년 1회 필기', '2020년 1회 필기'), ('2020년 2회 필기', '2020년 2회 필기'), ('2020년 3회 필기', '2020년 3회 필기'), ('2021년 1회 필기', '2021년 1회 필기'), ('2021년 2회 필기', '2021년 2회 필기'), ('2021년 3회 필기', '2021년 3회 필기'), ('2022년 1회 필기', '2022년 1회 필기'), ('2022년 2회 필기', '2022년 2회 필기')], max_length=255, verbose_name='출제 유형'),
        ),
    ]
