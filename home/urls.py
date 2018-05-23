from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url('home/', views.homepage, name='home'),
    url('base/', views.baseone, name='base'),
    url('index/', views.index, name='index'),
    url('register/', views.register, name='register'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),


    ]