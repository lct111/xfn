from django.views.generic import View
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse,JsonResponse
from .models import *
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
# from comments.forms import PlForm
from comments.models import Comments
from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMultiAlternatives
from itsdangerous import TimedJSONWebSignatureSerializer
from .form import *


# Create your views here.


def checklogin(fun):
    def check(self, req, *args):
        if req.user and req.user.is_authenticated:
            return fun(self, req, *args)
        else:
            return redirect(reverse('foods:login'))
    return check



class IndexView(View):
    @checklogin
    def get(self, req):
        adss = Adss.objects.all()

        food = Foods.objects.all()[:3]

        return render(req, 'foods/index.html', locals())


class SingleBlogView(View):
    @checklogin
    def get(self, req, id):
        # pf = PlForm()
        cc = Comments.objects.all()
        food = get_object_or_404(Foods, pk=id)
        food.view += 1
        food.save()

        return render(req, 'foods/blog-single.html', locals())

    def post(self, req, id):
        # pf = PlForm(req.POST)
        # if pf.is_valid():
        #     c=pf.save(commit=False)
        #     c.food = get_object_or_404(Foods,pk=id)
        # c.save()
        cc = Comments()
        cc.name = req.POST.get('name')
        cc.email = req.POST.get('email')
        cc.url = req.POST.get('url')
        cc.content = req.POST.get('content')
        cc.food = Foods.objects.get(pk=id)
        cc.save()

        return redirect(reverse('foods:singleblog', args=(id,)))


class BlogView(View):
    @checklogin
    def get(self, req):
        food = Foods.objects.all()

        # 得到分页
        paginator = Paginator(food, 2)
        # 得到页面
        pagenum = req.GET.get('page')
        pagenum = 1 if pagenum == None else pagenum
        page = paginator.get_page(pagenum)
        page.path = '/blog/'
        return render(req, 'foods/blog.html', {'page': page,'req':req})


class ShopView(View):
    @checklogin
    def get(self, req):
        food = Foods.objects.all()

        # 得到分页
        paginator = Paginator(food, 3)
        # 得到页面
        pagenum = req.GET.get('page')
        pagenum = 1 if pagenum == None else pagenum
        page = paginator.get_page(pagenum)
        page.path = '/shop/'

        return render(req, 'foods/shop.html', {'page': page,'req':req})


class ShopSingleView(View):
    @checklogin
    def get(self, req, id):
        food = get_object_or_404(Foods, pk=id)

        return render(req, 'foods/single-shop.html', locals())


class CategrayView(View):
    @checklogin
    def get(self, req, id):
        category = get_object_or_404(Category, pk=id)

        food = category.foods_set.all()

        # 得到分页
        paginator = Paginator(food, 2)
        # 得到页面
        pagenum = req.GET.get('page')
        pagenum = 1 if pagenum == None else pagenum
        page = paginator.get_page(pagenum)
        page.path = '/category/'
        return render(req, 'foods/blog.html', {'page': page,'req':req})


class TagView(View):
    @checklogin
    def get(self, req, id):
        tag = get_object_or_404(Tag, pk=id)

        food = tag.foods_set.all()

        # 得到分页
        paginator = Paginator(food, 2)
        # 得到页面
        pagenum = req.GET.get('page')
        pagenum = 1 if pagenum == None else pagenum
        page = paginator.get_page(pagenum)
        page.path = '/tag/'
        return render(req, 'foods/blog.html', {'page': page,'req':req})


class LoginView(View):

    def get(self,req):
        adss = Adss.objects.all()
        food = Foods.objects.all()[:3]
        lf = MyUserLogin()
        rf = MyUserRegist()

        return render(req,'foods/login.html',locals())

    def post(self,req):
        username = req.POST.get('username')
        password = req.POST.get('password')
        verify = req.POST.get("verify")

        user = MyUser.objects.filter(username=username)
        if username:
            if user[0].check_password(password):
                if user[0].is_active:
                    user1 = authenticate(req, username=username, password=password)
                    login(req, user1)
                    return redirect(reverse('foods:index'))
                else:
                    lf = MyUserLogin()
                    rf = MyUserRegist()
                    adss = Adss.objects.all()
                    food = Foods.objects.all()[:3]
                    errormessage = '用户没激活'
                    return render(req, 'foods/login.html', locals())
            else:
                lf = MyUserLogin()
                rf = MyUserRegist()
                adss = Adss.objects.all()
                food = Foods.objects.all()[:3]
                errormessage = '密码错误'
                return render(req, 'foods/login.html', locals())
        else:
            lf = MyUserLogin()
            rf = MyUserRegist()
            adss = Adss.objects.all()
            food = Foods.objects.all()[:3]
            errormessage = '用户名不存在'
            return render(req, 'foods/login.html', locals())


class RegisteView(View):
    def get(self, req):
        pass

    def post(self,req):
        username = req.POST.get('username')
        password = req.POST.get('password')
        email = req.POST.get('email')
        user = MyUser.objects.create_user(username=username, email=email, password=password)
        #默认为未激活
        user.is_active = False
        user.save()

        # 向用户发送激活邮件
        userid = user.id
        from django.conf import settings

        util = TimedJSONWebSignatureSerializer(secret_key=settings.SECRET_KEY, )
        userid = util.dumps({"userid": userid}).decode("utf-8")

        info = "请点击激活   <a href='http://127.0.0.1:8000/active/%s/' > 点我激活 %s </a>" % (userid, username,)
        from django.conf import settings
        mail = EmailMultiAlternatives("请激活", info, settings.DEFAULT_FROM_EMAIL, [email])
        mail.content_subtype = "html"
        mail.send()

        if user:
            return redirect(reverse('foods:login'))

        else:
            lf = MyUserLogin()
            rf = MyUserRegist()
            errormessage = '注册失败'
            return render(req, 'foods/login.html', locals())

#注册激活路由
class ActiveView(View):
    def get(self, req, id):
        from django.conf import settings
        util = TimedJSONWebSignatureSerializer(secret_key=settings.SECRET_KEY)
        obj = util.loads(id)
        id = obj["userid"]
        print(id)
        user = MyUser.objects.filter(pk=id).first()
        if user:
            user.is_active = True
            user.save()
            return redirect(reverse("foods:login"))

#退出用户
class LogOutView(View):
    def get(self, req):
        logout(req)
        return redirect(reverse('foods:login'))

# #检查用户名是否存在
# class CheckUserNameView(View):
#     def get(self, req):
#         username = req.GET.get("username")
#         user = MyUser.objects.filter(username=username).first()
#
#         if user:
#             return JsonResponse({"statecode": "1"})
#         else:
#             return JsonResponse({"statecode": "0", "erro": "用户名不存在"})