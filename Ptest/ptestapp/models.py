from django.db import models

class nextquestion(models.Model):
	next_question=models.IntegerField()

class allquestion(models.Model):
	question_number=models.IntegerField()
	questions=models.TextField(max_length=200)

class questionanswer(models.Model):
	question_number=models.ForeignKey(allquestion, on_delete=models.CASCADE)
	answer_number=models.IntegerField()
	answers=models.TextField(max_length=200)

class resultqa(models.Model):
	question_number=models.IntegerField()
	answer_number=models.IntegerField()

class introvertqa(models.Model):
	question_number=models.IntegerField()
	answer_number=models.IntegerField()

class extrovertqa(models.Model):
	question_number=models.IntegerField()
	answer_number=models.IntegerField()	
