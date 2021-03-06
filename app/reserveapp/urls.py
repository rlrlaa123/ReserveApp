"""reserveapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from reservation import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^signup/$', views.SignupList.as_view()),
    url(r'^login/$', views.LoginList.as_view(),name='login'),
    url(r'^validation/$', views.ValidationList.as_view(),name='validation'),
    url(r'^notice/$', views.NoticeList.as_view()),
    url(r'^reservation/$', views.ReservationList.as_view()),
    url(r'^inquire/$', views.InquireList.as_view()),
    url(r'^inquire/(?P<pk>[0-9]+)/comment/$', views.CommentList.as_view()),
    url(r'^inquire/(?P<pk>[0-9]+)/$', views.InquireDetailList.as_view()),
    url(r'^check/$', views.CheckList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]