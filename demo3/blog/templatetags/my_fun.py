from ..models import Artical,Category,Tag,Adss
from django.template import Library

register=Library()


@register.simple_tag
def mytags(num=3):
    return Artical.objects.all().order_by('-creat_time')[:num]


@register.simple_tag
def getatcicals():

    return Artical.objects.dates('creat_time','month')


@register.simple_tag
def getcategory():

    return Category.objects.all()


@register.simple_tag
def gettags():
    return  Tag.objects.all()

@register.simple_tag
def getadss():
    return Adss.objects.all()