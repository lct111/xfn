from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(req):
    return HttpResponse('这是首页')

def list(req):
    return HttpResponse('这是列表页')

def detail(req,id):
    return HttpResponse('这是详情页%s'%(id,))