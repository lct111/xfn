from django.conf.urls import url
from .views import *
from .feed import ArticalFeed
app_name='blog'

urlpatterns = [
    url(r'^$',IndexView.as_view(),name='index'),
    url(r'^single/(\d+)/$',SingleView.as_view(),name='single'),
    url(r'^atitle/(\d+)/(\d+)/$',AtitleView.as_view(),name='atitle'),
    url(r'^category/(\d+)/$',CategoryView.as_view(),name='category'),
    url(r'^tags/(\d+)/$',TagView.as_view(),name='tags'),
    url(r'^contact/$',ContactView.as_view(),name='contact'),
    url(r'^sendmail/$',SendmailView.as_view(),name='sendmail'),
    url(r'^rss/$',ArticalFeed(),name='rss'),
]