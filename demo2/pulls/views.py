from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Toup,MyUser
from django.template import loader
from django.views.generic import View
from .form import MyUserLogin,MyUserRegist
from django.contrib.auth import authenticate,login,logout


# Create your views here.

def checklogin(fun):
    def check(self,req,*args):
        #session方法
        # if req.session.get('username'):
        #     return fun(self,req,*args)

        #cookies方法
        # if req.COOKIES.get('username'):
        #     return fun(self,req,*args)
        if req.user and req.user.is_authenticated:
            return fun(self,req,*args)
        else:
            return redirect(reverse('pulls:login'))
    return check


class IndexView(View):
    @checklogin
    def get(self,req):
        question = Question.objects.all()
        res = loader.get_template('pulls/index.html').render({'question': question,'req':req})
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
        lf=MyUserLogin()
        rf=MyUserRegist()
        return render(req,'pulls/login_regist.html',locals())

    def post(self,req):
        username=req.POST.get('username')
        password=req.POST.get('password')

        user=authenticate(req,username=username,password=password)
        if user:
            login(req,user)
            return redirect(reverse('pulls:index'))

        else:
            lf = MyUserLogin()
            rf = MyUserRegist()
            errormessage='登录失败'
            return render(req,'pulls/login_regist.html',locals())


class RegisteView(View):
    def get(self,req):
        pass
    def post(self,req):
        username=req.POST.get('username')
        password=req.POST.get('password')
        email=req.POST.get('email')

        user=MyUser.objects.create_user(username=username,email=email,password=password)
        if user:
            return redirect(reverse('pulls:login'))

        else:
            lf=MyUserLogin()
            rf=MyUserRegist()
            errormessage='注册失败'
            return render(req,'pulls/login_regist.html',locals())


class LogOutView(View):
    def get(self,req):
        logout(req)
        return redirect(reverse('pulls:login'))
