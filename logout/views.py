from django.shortcuts import render
from django.http import HttpResponse
import os
import collections
import json
from django.contrib.sessions.backends.db import SessionStore
from django.core.files import File as FileWrapper
from django.conf import settings
from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.views.decorators.csrf import ensure_csrf_cookie, requires_csrf_token






def logout(request):
   try:
      del request.session['mail']
   except:
      pass
   return HttpResponse("<strong>You are logged out.</strong>")# Create your views here.
