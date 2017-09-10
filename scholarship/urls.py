from . import views
from django.conf.urls import include, url
from django.contrib import admin
urlpatterns = [
    url(r'^$',views.scholarship, name='scholarship'),
    url(r'^recommended/$',views.recommended, name='recommended'),
    url(r'^view_profile/$',views.view_profile, name='view_profile'),
    url(r'^edit_profile/$',views.edit_profile, name='edit_profile'),
    url(r'^applications/$',views.applications, name='applications'),
    url(r'^get_scholarship/$',views.get_scholarship, name='scholarship'),
    url(r'^getinfo/$',views.getinfo, name='info'),
    url(r'^filters/$',views.filters, name='filters'),
    url(r'^upload_docs/$',views.upload_docs,name="upload_docs"),
    url(r'^applied_for/$',views.applied_for, name='apply'),
    url(r'^getmedical/$',views.getmedical, name='medical'),
    url(r'^gettrans/$',views.gettrans, name='transcripts')
]
