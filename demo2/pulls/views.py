from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Toup
from django.template import loader
from django.views.generic import View


# Create your views here.

class IndexView(View):

    def get(self,req):
        question = Question.objects.all()

        res = loader.get_template('pulls/index.html').render({'question': question})
        return HttpResponse(res)

class ToupView(View):
    def get(self,req, id):
        ques = Question.objects.get(pk=id)
        # res=loader.get_template('pulls/toup.html').render({'ques':ques})
        return render(req, 'pulls/toup.html', {'ques': ques})

    def post(self,req,id):
        r_id = req.POST.get('info')
        tt = Toup.objects.get(pk=r_id)
        tt.vote += 1
        tt.save()
        return HttpResponseRedirect('/result/%s/' % (id,))

class ResultView(View):
    def get(self,req, id):
        question = Question.objects.get(pk=id)
        res = loader.get_template('pulls/result.html').render({'question': question})
        return HttpResponse(res)
