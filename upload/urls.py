from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^$',views.upload,name="upload"),
	url(r'^resume/$',views.resume,name="upload"),
	url(r'^fill_details/$',views.fill_details,name="form")
]