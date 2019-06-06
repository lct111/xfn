from django.conf.urls import url
from .views import index,list,detail,deletehero,deletebook
app_name='booktest'


urlpatterns=[
    url(r'^$',index,name='index'),
    url(r'^list/$',list,name='list'),
    url(r'^detail/(\d+)/$',detail,name='detail'),

    url(r'^deletehero/(\d+)/$',deletehero,name='deletehero'),
    url(r'^deletebook/(\d+)/$',deletebook,name='deletebook')
]