from django.conf.urls import url
from .views import index,toup,result
app_name='pulls'

urlpatterns=[
    url(r'^$',index,name='index'),
    url(r'^toup/(\d+)/$',toup,name='toup'),
    url(r'^result/(\d+)/$',result,name='result'),
]