# Generated by Django 4.0 on 2021-12-23 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='allquestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_number', models.IntegerField(max_length=2)),
                ('questions', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='questionanswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_numner', models.IntegerField(max_length=2)),
                ('anwsers', models.TextField(max_length=200)),
                ('question_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ptestapp.allquestion')),
            ],
        ),
    ]