"""mysite URL Configuration

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
#staticフォルダを有効にする為の関数
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^content/', include('nayameru_student.urls', namespace='nayameru_student')),
    #url(r'^top/',   include('nayameru_student.urls', namespace='nayameru_student')),
    url(r"^auth/", include("userauth.urls", namespace="userauth")),
    url(r"^login/$", "userauth.views.login", name="login"),
    url(r"^logout/$", "userauth.views.logout", name="logout"),
]

#staticフォルダを有効にする
urlpatterns += staticfiles_urlpatterns()
