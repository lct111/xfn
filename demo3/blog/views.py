from django.shortcuts import render,redirect,reverse
from django.views.generic import View
from django.shortcuts import get_object_or_404
from .models import *
from django.core.paginator import Paginator
import markdown
from django.core.mail import send_mail,EmailMultiAlternatives
from demo3 import settings
from django.http import HttpResponse
from comments.forms import PlForm

# Create your views here.

class IndexView(View):

    def get(self,req):
        artical = Artical.objects.all()

        #得到分页
        paginator = Paginator(artical,1)
        #得到页面
        pagenum=req.GET.get('page')
        pagenum = 1 if pagenum == None else pagenum
        page = paginator.get_page(pagenum)
        page.path = '/'

        return render(req,'blog/index.html',{'page':page})

class SingleView(View):

    def get(self,req,id):
        pf = PlForm()
        artical = get_object_or_404(Artical,pk=id)

        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ])
        artical.content = md.convert(artical.content)
        artical.toc=md.toc

        return render(req,'blog/single.html',locals())

    def post(self,req,id):
        # tt= Pinglun()
        # tt.name=req.POST.get('name')
        # tt.email=req.POST.get('email')
        # tt.url=req.POST.get('url')
        # tt.content=req.POST.get('content')
        # artical=Artical.objects.get(pk=id)
        # tt.artical=artical
        # tt.save()
        pf=PlForm(req.POST)

        if pf.is_valid():
            c=pf.save(commit=False)
            c.artical = get_object_or_404(Artical,pk=id)

        c.save()
        return redirect(reverse('blog:single',args=(id,)))

class AtitleView(View):

    def get(self,req,year,month):
        artical = Artical.objects.filter(creat_time__year=year,creat_time__month=month)

        # 得到分页
        paginator = Paginator(artical, 1)
        # 得到页面
        pagenum = req.GET.get('page')
        pagenum = 1 if pagenum == None else pagenum
        page = paginator.get_page(pagenum)
        page.path = '/atitle/%s/%s/'%(year,month)
        return render(req,'blog/index.html',{'page':page})

class CategoryView(View):

    def get(self,req,id):
        category=get_object_or_404(Category,pk = id)
        artical = category.artical_set.all()

        # 得到分页
        paginator = Paginator(artical, 1)
        # 得到页面
        pagenum = req.GET.get('page')
        pagenum = 1 if pagenum == None else pagenum
        page = paginator.get_page(pagenum)
        page.path = '/category/%s/' %(id,)
        return render(req, 'blog/index.html', {'page':page})

class TagView(View):

    def get(self,req,id):
        tag = get_object_or_404(Tag,pk = id)
        artical = tag.artical_set.all()

        # 得到分页
        paginator = Paginator(artical, 1)
        # 得到页面
        pagenum = req.GET.get('page')
        pagenum = 1 if pagenum == None else pagenum
        page = paginator.get_page(pagenum)
        page.path = '/tags/%s/' % (id,)
        return render(req, 'blog/index.html', {'page': page})

class SendmailView(View):

    def get(self,req):
        try:
            mail = EmailMultiAlternatives(subject="测试邮件html格式",
                                          body="<h1>  <a href = 'http://www.baidu.com'> 百度 </a>  </h1>",
                                          from_email=settings.DEFAULT_FROM_EMAIL,
                                          to=["18837597987@163.com", "zhangzhaoyu@qikux.com"])
            mail.content_subtype = "html"
            mail.send()

            return HttpResponse('发送成功')

        except:
            return HttpResponse('发送失败')



class ContactView(View):

    def get(self,req):
        return render(req,'blog/contact.html')

    def post(self,req):
        email = req.POST.get('email')
        info = req.POST.get('message')

        message = MessageInfo()
        message.email = email
        message.info = info
        message.save()

        return HttpResponse('建议成功')
