from django.contrib import admin
from . import views
from django.conf.urls import include,url


urlpatterns = [
   #Homepage
    url(r'^$',views.index,name='index'),

    # /music/id/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

]