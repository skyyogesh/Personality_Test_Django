# Generated by Django 4.0 on 2021-12-23 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ptestapp', '0002_alter_allquestion_question_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='nextquestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('next_question', models.IntegerField()),
            ],
        ),
    ]
