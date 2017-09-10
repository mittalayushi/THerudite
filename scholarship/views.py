from django.shortcuts import render
from django.http import HttpResponse
import os
import collections
from upload.models import User,Scholarship
from havenondemand.hodclient import *
import json
from django.contrib.sessions.backends.db import SessionStore
from django.core.files import File as FileWrapper
from django.conf import settings
from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect
from django.views.decorators.csrf import ensure_csrf_cookie, requires_csrf_token
from organisations.models import org, scheme

 # uncomment if using local file


@requires_csrf_token
def scholarship(request):
	if request.method == "POST":
		if request.is_ajax():
			if request.session.has_key('mail'):
				emailx = request.session['mail']
				user=User.objects.get(email=emailx)
				print (emailx)
				for filename, file in request.FILES.iteritems():
					user.resume = request.FILES[filename]
				print(user.resume)
				user.save()
				return HttpResponse("hey")



def getinfo(request):
	print('hello')
	if request.method=="POST":
		if request.is_ajax():
			category=request.POST.get('category')
			print(category)
			income=request.POST.get('income')
			physically_handicapped=request.POST.get('ph')
			if request.session.has_key('mail'):
				emailx=request.session['mail']
				user=User.objects.get(email=emailx)
				print(user.name)
				user.category = category
				user.income = income
				user.physically_handicapped = physically_handicapped
				user.save()
				print(user.physically_handicapped)
				return HttpResponse('hey')
	else:
		return HttpResponseNotFound("You are smart.. You know what to do before having access to this site ;)")



def recommended(request):
	if request.session.has_key('mail'):
		emailx=request.session['mail']
		user=User.objects.get(email=emailx)
		user_name=user.name
		user_name=user_name.split(" ")
		uname=user_name[0]
		recommendations=[]
		for Result in org.objects.all():
			for obj in Result.schemes:
				print(obj.name)
				if (set(obj.tags).issubset(set(user.tags))):
					print(obj.tags)
					print(user.tags)
					print('yes')
					obj.org_name=Result.name
					obj.org_id=Result.id
					obj.save()
					recommendations.append(obj)
					recommendations=list(set(recommendations))
					print(recommendations)
		return render(request,'recommended/recommended.html',{"recommendations":recommendations,"user_name":user.name})
		#return render(request,'recommended/recommended.html',{"user_name":uname})	
	else:
		return HttpResponseNotFound("You are smart.. You know what to do before having access to this site ;)")



'''def docs(request):
	if request.method == "POST":
		if request.is_ajax():
			Docs=DocsUpload()
			print (request.FILES)
			#i=0
			for filename, file in request.FILES.getlist('file'):
				print(request.FILES[filename])
			print(Docs.docs)			
			return HttpResponse('hello')
'''
def get_scholarship(request):
	if request.session.has_key('mail'):
		user=User.objects.get(email=request.session['mail'])
		if request.method=="POST":
			if request.is_ajax():
				print('hello')
				tags=[]
				user.field=request.POST.get('field')
				if user.field!='NULL':
					tags.append(user.field)
				user.category=request.POST.get('category')
				if user.category!='NULL':
					tags.append(user.category)
				user.gender=request.POST.get('gender')
				if user.gender!='NULL':
					tags.append(user.gender)
				if request.POST.get('overseas')=='yes':
					user.overseas='overseas'
					tags.append('overseas')
				user.sports=request.POST.get('sports')
				if user.sports!='NULL':
					tags.append(user.sports)
				if request.POST.get('physically_handicapped')=='yes':
					user.physically_handicapped='disability'
					tags.append('disability')
				user.education=request.POST.get('edu')
				tags.append(user.education)
				user.income_ceiling=request.POST.get('income')
				tags.append(user.income_ceiling)
				user.tags=tags
				user.save()
				return HttpResponseRedirect('/scholarship/recommended/')


def applied_for(request):
	if request.session.has_key('mail'):
		emailx=request.session['mail']
		user=User.objects.get(email=emailx)
		org_id=request.POST.get('id')
		name=request.POST.get('name')
		flag=0
		for obj in user.scholarship:
			print (obj)
			if(obj.identification==org_id and obj.name==name):
				flag=1
		if (flag==0):
			user.scholarship.append(Scholarship(identification=org_id,name=name))
			user.save()
			return HttpResponse('hey')
		else:
			return HttpResponse('Already applied')
	else:
		return HttpResponseNotFound("You are smart.. You know what to do before having access to this site ;)")


def upload_docs(request):
	if request.session.has_key('mail'):
		emailx=request.session['mail']
		user=User.objects.get(email=emailx)
		name=user.name
		name=name.split(" ")
		return render(request,'upload/upload_docs.html',{"name":name[0],"user":user})



def getmedical(request):
	if request.session.has_key('mail'):
		emailx=request.session['mail']
		user=User.objects.get(email=emailx)
		if request.method == 'POST':
			if request.is_ajax():
				for filename, file in request.FILES.iteritems():
					user.physical_medical=request.FILES[filename]
				user.save()
				return HttpResponse("hey")
	else:
		return HttpResponseNotFound("You are smart.. You know what to do before having access to this site ;)")




def gettrans(request):
	if request.session.has_key('mail'):
		emailx=request.session['mail']
		user=User.objects.get(email=emailx)
		if request.method == 'POST':
			if request.is_ajax():
				for filename, file in request.FILES.iteritems():
					#filename=user.id
					#request.FILES[filename]="trans/"+user.id
					user.transcripts=request.FILES[filename]
				user.save()
				return HttpResponse("hey")
	else:
		return HttpResponseNotFound("You are smart.. You know what to do before having access to this site ;)")



def applications(request):
	if request.session.has_key('mail'):
		emailx=request.session['mail']
		user=User.objects.get(email=emailx)
		return render(request,'applications/applications.html',{"applications":user.scholarship,"name":user.name})
	else:
		return HttpResponseNotFound("You are smart.. You know what to do before having access to this site ;)")



#			return render(request,'recommended/recommended.html',{"recommendations":recommendations})	



		'''if request.method == "POST":
		if request.is_ajax():
			if request.session.has_key('mail'):
				emailx = request.session['mail']
				user=User.objects.get(email=emailx)
				print (emailx)
				for filename, file in request.FILES.iteritems():
					user.resume = request.FILES[filename]
				print(user.resume)
				user.save()
				return HttpResponse("hey")
'''

def view_profile(request):
	if request.session.has_key('mail'):
		emailx=request.session['mail']
		user=User.objects.get(email=emailx)
		return render(request,'view_profile.html',{"user":user})
	else:
		return HttpResponseNotFound("You are smart.. You know what to do before having access to this site ;)")

def edit_profile(request):
	if request.session.has_key('mail'):
		emailx=request.session['mail']
		user=User.objects.get(email=emailx)
		if request.method == 'POST':
			if request.is_ajax():
				name=request.POST.get('name')
				gender=request.POST.get('gender')
				dob=request.POST.get('dob')
				#income=request.POST.get('income')
				only_girl=request.POST.get('girl_child')
				physically_handicapped=request.POST.get('physically_handicapped')
				category=request.POST.get('category')
				if user.name!=None:
					user.name=name
				if user.d_o_b!=None:
					user.d_o_b=dob
				if user.gender!=None:
					user.gender=gender
				if user.only_girl!=None:
					user.only_girl=only_girl
				if user.category!=None:
					user.category=category
				if user.physically_handicapped!=None:
					user.physically_handicapped=physically_handicapped
				user.save()
				#user.income=income
				return HttpResponseRedirect('/scholarship/view_profile/')
		return render(request,'edit_profile.html',{"user":user})
	else:
		return HttpResponseNotFound("You are smart.. You know what to do before having access to this site ;)")	


def filters(request):
	if request.session.has_key('mail'):
		return render(request,'filters.html')