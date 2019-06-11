from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Toup
from django.template import loader
from django.views.generic import View


# Create your views here.

def checklogin(fun):
    def check(self,req,*args):
        #session方法
        if req.session.get('username'):
            return fun(self,req,*args)

        #cookies方法
        # if req.COOKIES.get('username'):
        #     return fun(self,req,*args)
        else:
            return redirect(reverse('pulls:login'))
    return check


class IndexView(View):
    @checklogin
    def get(self,req):
        question = Question.objects.all()

        res = loader.get_template('pulls/index.html').render({'question': question})
        return HttpResponse(res)

class ToupView(View):
    @checklogin
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
    @checklogin
    def get(self,req, id):
        question = Question.objects.get(pk=id)
        res = loader.get_template('pulls/result.html').render({'question': question})
        return HttpResponse(res)

class LoginView(View):

    def get(self,req):
        return render(req,'pulls/login.html')

    def post(self,req):
        username=req.POST.get('username')
        pwd=req.POST.get('password')

        #session方法
        req.session['username']=username
        return redirect(reverse('pulls:index'))

        #cookie方法
        # res=redirect(reverse('pulls:index'))
        # res.set_cookie('username',username)
        # return res