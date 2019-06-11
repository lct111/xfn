from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Toup
from django.template import loader


# Create your views here.

def index(req):
    question = Question.objects.all()

    res = loader.get_template('pulls/index.html').render({'question': question})
    return HttpResponse(res)


def toup(req, id):
    ques = Question.objects.get(pk=id)

    # res=loader.get_template('pulls/toup.html').render({'ques':ques})
    if req.method == 'GET':
        return render(req, 'pulls/toup.html', {'ques': ques})

    elif req.method == 'POST':
        r_id = req.POST.get('info')
        tt = Toup.objects.get(pk=r_id)
        tt.vote += 1
        tt.save()
        return HttpResponseRedirect('/result/%s/' % (ques.id,))


def result(req, id):
    question = Question.objects.get(pk=id)

    res = loader.get_template('pulls/result.html').render({'question': question})
    return HttpResponse(res)
