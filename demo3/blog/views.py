from django.shortcuts import render,redirect,reverse
from django.views.generic import View
from .models import *
from comments.models import Pinglun

# Create your views here.

class IndexView(View):

    def get(self,req):
        artical = Artical.objects.all()
        return render(req,'blog/index.html',locals())

class SingleView(View):

    def get(self,req,id):
        artical = Artical.objects.get(pk=id)
        return render(req,'blog/single.html',locals())

    def post(self,req,id):
        tt= Pinglun()
        tt.name=req.POST.get('name')
        tt.email=req.POST.get('email')
        tt.url=req.POST.get('url')
        tt.content=req.POST.get('content')
        artical=Artical.objects.get(pk=id)
        tt.artical=artical
        tt.save()
        return redirect(reverse('blog:single',args=id))