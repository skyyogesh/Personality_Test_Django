from django.shortcuts import render
from django.http import HttpResponse, Http404 
from django.template import loader, RequestContext
from . models import allquestion, questionanswer, nextquestion , resultqa , introvertqa , extrovertqa

def ptest_home(request):
    template = loader.get_template('starttest.html')
    return HttpResponse(template.render())

def ptest_qa(request):
    qno=0
    ansno=0
    if (request.POST):
        click = request.POST.get('btn')
        qno = int(request.POST.get('questionno'))
        if click == "Next":
            ansno = request.POST.get('answer')
            nextquestion.objects.all().delete()
            nq = qno + 1
            nextquestion.objects.create(next_question=nq)
            resultqa.objects.filter(question_number=qno).delete()
            resultqa.objects.create(question_number=qno,answer_number=ansno)
        elif click == "Previous":
            nextquestion.objects.all().delete()
            nq = qno - 1
            nextquestion.objects.create(next_question=nq)
        elif click == "Finish":
            ansno = request.POST.get('answer')
            resultqa.objects.filter(question_number=qno).delete()
            resultqa.objects.create(question_number=qno,answer_number=ansno)
            queryset_res_qa=resultqa.objects.all()
            queryset_iqa = introvertqa.objects.all()
            queryset_eqa = extrovertqa.objects.all()
            introvert=0;
            extrovert=0;
            for i in queryset_res_qa:
                for j in queryset_iqa:
                    if i.question_number == j.question_number and i.answer_number == j.answer_number:
                        introvert += 1

                for k in queryset_eqa:
                    if i.question_number == k.question_number and i.answer_number == k.answer_number:
                        extrovert += 1

            context = {}
            introvert_msg = ["1. You feel that living alone is to live happily, and you prefer hiding in a crowd rather than standing out in one.",
                            "2. You are perpetually tormented by the idea of doing things wrong, not understanding or not being alert enough or intelligent enough to do what others expect of you." ,
                            "3. You lack in self-confidence and you seem to believe that others are better than you." ,
                            "4. While in a conversation, for example, you would be more likely to go along with the other’s points of view as you don’t fully respect your own opinions." ,
                            "5. Where there’s a low level task to complete or a service to be allotted, it’s you who volunteers." ,
                            "6. When people want to get out of a task, they naturally come to you as they know that you never say ‘no’."]

            extrovert_msg = ["1. Whether at work or at home, you are a leader, the head of the pack." , 
                            "2. You are the type of person who is at ease with everyone — with the grocer, the doctor, a managing director or a waiter.",
                            "3. You have an opinion about just about everything and you like to share your knowledge around, even imposing it on others if they haven’t asked for it." ,
                            "4. Your personal and professional entourages easily class you as a ‘loud mouth’, sure about yourself, not in the least bit bothered about what others think of you and someone who occasionally likes to play the card of provocation.",
                            "5. When you’re on a roll, it’s hard to sop you and the least that could be said is that listening skills are not one of your innate skills.",
                            "6. In the couples arena, you have maybe fallen for someone with a similar temperament – making for animated evenings! Or on the contrary, you live with a more introverted partner over whom you can, in some cases, have the upper hand"]


            if introvert > extrovert :
                context = {
                    'int_ext':'Introvert',
                    'msg': introvert_msg,
                }
            else :
                context = {
                    'int_ext':'Extrovert',
                    'msg':extrovert_msg,
                }
            return render(request,"result.html",context)                
    else:
        nextquestion.objects.all().delete()
        nextquestion.objects.create(next_question=1)
        resultqa.objects.all().delete()

    queryset_nq=nextquestion.objects.first()
    next_ques=queryset_nq.next_question
    queryset_allq=allquestion.objects.all()
    tot_q = queryset_allq.count()
    queryset_aq=allquestion.objects.filter(question_number=next_ques)
    next_q=0
    for x in queryset_aq:
        next_q=x.question_number

    queryset_qa=questionanswer.objects.filter(question_number=next_q)
    queryset_rqa=resultqa.objects.filter(question_number=next_q)
    for z in queryset_rqa:
        print(z.answer_number)
    context={
        'curr_q':next_ques,
        'total_q':tot_q,
        'aq':queryset_aq,
        'qa':queryset_qa,
        'rqa':queryset_rqa,
    }

    return render(request,"qapage.html",context)



