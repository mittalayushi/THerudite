from django.conf.urls import patterns, include, url
from . import views
from django.conf.urls import include, url
from django.contrib import admin
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
   url(r'^$', views.index, name='home'),
   url(r'^add_remove', views.add_remove, name='add_remove'),
   url(r'^remove_scholarship', views.index, name='remove_scholarship'),
   url(r'^view_scholarship', views.view_scholarship, name='view_scholarship'),
   url(r'^signup',views.signup,name='signup'),
   url(r'^contact',views.contact,name='contact'),
   url(r'^add_scholarship',views.add_scholarship,name='add_scholarship'),
   url(r'^logout',views.logout,name='logout'),
]
