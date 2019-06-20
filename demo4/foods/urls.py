from django.conf.urls import url
from .views import *
from haystack.views import SearchView

app_name = 'foods'

urlpatterns = [
    url(r'^$',IndexView.as_view(),name='index'),
    url(r'^singleblog/(\d+)/$',SingleBlogView.as_view(),name='singleblog'),
    url(r'^blog/$',BlogView.as_view(),name='blog'),
    url(r'^shop/$',ShopView.as_view(),name='shop'),
    url(r'^shopsingle/(\d+)/$',ShopSingleView.as_view(),name='shopsingle'),
    url(r'^category/(\d+)/$',CategrayView.as_view(),name='category'),
    url(r'^tag/(\d+)/$',TagView.as_view(),name='tag'),
    url(r'^login/$',LoginView.as_view(),name='login'),
    url(r'^regist/$',RegisteView.as_view(),name='regist'),
    url(r'^active/(.*?)/$',ActiveView.as_view(), name="active"),
    url(r'^logout/$',LogOutView.as_view(),name='logout'),
    # url(r'^checkusername/$',CheckUserNameView.as_view(), name="checkusername"),
    url(r'^search/$',SearchView(),name="search"),
]
