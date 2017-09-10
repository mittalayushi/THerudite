from . import views
from django.conf.urls import include, url
from django.contrib import admin
urlpatterns = [
    url(r'^student/$',views.stu_signup, name='signup'),
    url(r'^organisations/$',views.org_signup, name='signup'),
]
