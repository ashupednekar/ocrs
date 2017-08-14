from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^complainant/$', views.complainant),
    url(r'^complainant/clogin',views.clogin)
]