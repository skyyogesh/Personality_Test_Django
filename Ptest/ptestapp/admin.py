from django.contrib import admin

from . models import allquestion, questionanswer, nextquestion, introvertqa ,extrovertqa, resultqa

admin.site.register(allquestion)
admin.site.register(questionanswer)
admin.site.register(nextquestion)
admin.site.register(resultqa)
admin.site.register(introvertqa)
admin.site.register(extrovertqa)
