from django.conf.urls import url
from .views import index,list,detail

urlpatterns=[
    url(r'^$',index),
    url(r'list/',list),
    url(r'^detail/(\d+)/$',detail),
]