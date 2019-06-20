from ..models import Foods,Category,Tag
from django.template import Library

register = Library()

@register.simple_tag
def getfood(num=8):
    return Foods.objects.all().order_by('-creat_time')[:num]

@register.simple_tag
def getcategory():
    return Category.objects.all()

@register.simple_tag
def getfoods(num=3):
    return Foods.objects.all().order_by('-creat_time')[:num]

@register.simple_tag
def gettag():
    return Tag.objects.all()

# @register.simple_tag
# def getres():
#     return Tag.objects.all()