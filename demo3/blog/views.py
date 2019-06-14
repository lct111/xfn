from django.shortcuts import render,redirect,reverse
from django.views.generic import View
from django.shortcuts import get_object_or_404
from .models import *

from comments.forms import PlForm

# Create your views here.

class IndexView(View):

    def get(self,req):
        artical = Artical.objects.all()
        return render(req,'blog/index.html',locals())

class SingleView(View):

    def get(self,req,id):
        pf = PlForm()
        artical = get_object_or_404(Artical,pk=id)
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

        return render(req,'blog/index.html',locals())

class CategoryView(View):

    def get(self,req,id):
        category=get_object_or_404(Category,pk = id)
        artical = category.artical_set.all()

        return render(req, 'blog/index.html', locals())

class TagView(View):

    def get(self,req,id):
        tag = get_object_or_404(Tag,pk = id)
        artical = tag.artical_set.all()
        return render(req,'blog/index.html',locals())

