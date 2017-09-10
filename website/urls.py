from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
	url(r'^index/',include('start.urls')),
	url(r'^signup/',include('signup.urls')),
	url(r'^logout/',include('logout.urls')),
	url(r'^upload/',include('upload.urls')),
	url(r'^scholarship/',include('scholarship.urls')),
	url(r'^organisations/',include('organisations.urls')),
	#url(r'^upload/',include('upload.urls')),
    url(r'^admin/', admin.site.urls),
]
