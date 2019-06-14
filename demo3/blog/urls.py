from django.conf.urls import url
from .views import *
app_name='blog'

urlpatterns = [
    url(r'^$',IndexView.as_view(),name='index'),
    url(r'^single/(\d+)/$',SingleView.as_view(),name='single'),
    url(r'^atitle/(\d+)/(\d+)/$',AtitleView.as_view(),name='atitle'),
    url(r'^category/(\d+)/$',CategoryView.as_view(),name='category'),
    url(r'^tags/(\d+)/$',TagView.as_view(),name='tags'),
]