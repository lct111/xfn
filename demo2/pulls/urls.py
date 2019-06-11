from django.conf.urls import url
from .views import *
app_name='pulls'

urlpatterns=[
    url(r'^$',IndexView.as_view(),name='index'),
    url(r'^toup/(\d+)/$',ToupView.as_view(),name='toup'),
    url(r'^result/(\d+)/$',ResultView.as_view(),name='result'),
    url(r'^login/$',LoginView.as_view(),name='login'),
]