from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
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

        print(MyUser.objects.filter(username=username))
        user=authenticate(req,username=username,password=password)
        print(user)
        print("+++++++++++")
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

class CheckUserNameView(View):
    def get(self,req):
        username = req.GET.get("username")
        print(MyUser.objects.filter(username = username))
        # for r in MyUser.objects.filter(username = username):
        #     print('++',r.username,'++')
        user = MyUser.objects.filter(username = username).first()

        if user:
            return JsonResponse({"statecode":"1"} )
        else:
            return JsonResponse({"statecode":"0","error":"用户名不存在"})

import random,io
from PIL import Image,ImageDraw,ImageFont

class VerifyView(View):

    def get(self,req):
        # 应该返回图片
        # 定义变量，用于画面的背景色、宽、高
        bgcolor = (random.randrange(20, 100),
                   random.randrange(20, 100),
                   random.randrange(20, 100))
        width = 100
        heigth = 25
        # 创建画面对象
        im = Image.new('RGB', (width, heigth), bgcolor)
        # 创建画笔对象
        draw = ImageDraw.Draw(im)

        # 调用画笔的point()函数绘制噪点
        for i in range(0, 100):
            xy = (random.randrange(0, width), random.randrange(0, heigth))
            fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
            draw.point(xy, fill=fill)

        # 定义验证码的备选值
        str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
        # 随机选取4个值作为验证码
        rand_str = ''
        for i in range(0, 4):
            rand_str += str1[random.randrange(0, len(str1))]
        # 构造字体对象
        font = ImageFont.truetype('calibrib.ttf', 23)
        fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
        # 绘制4个字
        draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
        draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
        draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
        draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
        # 释放画笔
        del draw
        req.session['verifycode'] = rand_str
        f = io.BytesIO()
        im.save(f, 'png')
        # 将内存中的图片数据返回给客户端，MIME类型为图片png
        return HttpResponse(f.getvalue(), 'image/png')

