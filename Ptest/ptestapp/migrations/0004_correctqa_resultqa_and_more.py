# Generated by Django 4.0 on 2021-12-27 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ptestapp', '0003_nextquestion'),
    ]

    operations = [
        migrations.CreateModel(
            name='correctqa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_number', models.IntegerField()),
                ('answer_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='resultqa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_number', models.IntegerField()),
                ('answer_number', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='questionanswer',
            old_name='answer_numner',
            new_name='answer_number',
        ),
    ]
