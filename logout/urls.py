from . import views
from django.conf.urls import include, url
from django.contrib import admin
urlpatterns = [
    url(r'^$',views.logout, name='logout')
]
