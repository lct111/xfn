from django.conf.urls import url
from .views import *

app_name='pulls'

urlpatterns=[
    url(r'^$',IndexView.as_view(),name='index'),
    url(r'^toup/(\d+)/$',ToupView.as_view(),name='toup'),
    url(r'^result/(\d+)/$',ResultView.as_view(),name='result'),
    url(r'^login/$',LoginView.as_view(),name='login'),
    url(r'^regist/$',RegisteView.as_view(),name='regist'),
    url(r'^logout/$',LogOutView.as_view(),name='logout'),
    url(r'^checkusername/$',CheckUserNameView.as_view(), name="checkusername"),
    url(r'^verify/$',VerifyView.as_view(), name="verify"),

]