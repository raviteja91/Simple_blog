"""first URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from blog.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
	url(r'^post/$', 'blog.views.main', name='main'),
	url(r'^add/post/$', 
        'blog.views.add_post', 
        name='blog_add_post'),
	url(r'^post/(?P<post_id>[0-9]+)/$', 
        'blog.views.view_post',
        name='blog_post_detail'),
    #(r"^post/", "post"),
    #(r"^add_comment/(\d+)/$", "add_comment"),




]
