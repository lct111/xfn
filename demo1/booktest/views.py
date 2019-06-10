from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import BookInfo,HeroInfo
from django.template import loader

# Create your views here.

def index(req):
    # return HttpResponse('这是首页')
    temp=loader.get_template('booktest/index.html')
    res=temp.render({})
    return HttpResponse(res)

def list(req):
    books=BookInfo.objects.all()

    # return HttpResponse('这是列表页')
    res=loader.get_template('booktest/list.html').render({'books':books})
    return HttpResponse(res)

def detail(req,id):
    book=BookInfo.objects.get(pk=id)
    # return HttpResponse('这是详情页%s'%(id,))
    res=loader.get_template('booktest/detail.html').render({'book':book})
    # print(res)
    # result =
    # print(result)
    return HttpResponse(res)


def deletehero(req,id):
    hero = HeroInfo.objects.get(pk=id)
    hero.delete()

    return HttpResponseRedirect('/detail/%s/'%(hero.book.id,))

def deletebook(req,id):

    book=BookInfo.objects.get(pk=id)
    book.delete()

    return HttpResponseRedirect('/list/')

def addhero(req,id):
    book=BookInfo.objects.get(pk=id)
    if req.method=='GET':
        return render(req,'booktest/addhero.html',{'book':book})
    elif req.method=='POST':
        hero=HeroInfo()
        hero.name=req.POST.get('heroname')
        hero.content=req.POST.get('herocontent')
        hero.book=book
        hero.save()
        return HttpResponseRedirect('/detail/%s/'%(id,))