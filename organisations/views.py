# Create your views here.
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .forms import loginForm
from .forms import signupForm
from .forms import NewScholarshipForm
from django.contrib.sessions.backends.db import SessionStore
from django.core.exceptions import ObjectDoesNotExist
from .models import org,scheme

def index(request):
	form = loginForm()
	if request.method == 'POST':
		form = loginForm(request.POST)
		if form.is_valid():
			mail = request.POST['email']
			passw = request.POST['password']
			print(passw)
			try:
				print('kiss')
				user = org.objects.get(email=mail,password=passw)
				request.session['mail']=mail
				return HttpResponseRedirect('/organisations/add_remove/')
			except ObjectDoesNotExist:
				print('hug')
				return HttpResponse('no babe....wrong password')
    	return render(request, 'organisations/login.html' , {'form':form})


def add_remove(request):
	if request.session.has_key('mail'):
		#return HttpResponse('heelo')
		return render(request,'organisations/add_remove.html')
	else:
		return HttpResponse('fuck off man')



def signup(request):
	form = signupForm()
	if request.method == 'POST':
		form = signupForm(request.POST)
		if form.is_valid():
			print ('love you')
			try: 
				print(':*')
				mail = request.POST['email']
				user = org.objects.get(email=mail)
				return HttpResponse('mail exists...bht smart bn rhe ho')
			except ObjectDoesNotExist:
				print('miss you')
				user = org.objects.create(
					name = request.POST['org_name'],
					address = request.POST['address'],
					phone_no = request.POST['phone_no'],
					email = request.POST['email'],
					password = request.POST['password'],
					person = request.POST['name']
					)
				user.save()
				#return HttpResponse('We will stay in touch')
				#print request.POST['']
				return HttpResponseRedirect('/organisations/contact/')

	return render(request,'organisations/signup.html',{'form':form})

def contact(request):
	return render_to_response('organisations/contact.html')

def view_scholarship(request):
	if request.session.has_key('mail'):
		user = org.objects.get(email=request.session['mail'])
		return render(request,'organisations/view_scholarship.html',{'user':user})
	else:
		return HttpResponse('you know what to do')

def add_scholarship(request):
	form = NewScholarshipForm()
	if request.session.has_key('mail'):
		if request.method == 'POST':
			form = NewScholarshipForm(request.POST)
			if form.is_valid():
				#print ('kisses')
				#print (request.POST['scholarship_name'])
				emailx = request.session['mail']
				user = org.objects.get(email=emailx)
				tags=[]
				name = request.POST['scholarship_name']
				description = request.POST['description']
				category = request.POST['category']
				if category!="NULL":
					tags.append(category)
				gender = request.POST['gender']
				if gender!="NULL":
					tags.append(gender)
				Rate = request.POST['amount']
				education = request.POST['edu']
				if education!="":
					tags.append(education)
				overseas = request.POST['overseas']
				if overseas=='yes':
					tags.append('overseas')
				income_ceiling = request.POST['salary']
				if income_ceiling!="":
					tags.append(income_ceiling)
				disability = request.POST['disability']
				if disability=='yes':
					tags.append('disability')
				
				sports = request.POST['sports']
				if sports!='NULL':
					tags.append(sports)
				
				field = request.POST['field']
				if field!='NULL':
					tags.append(field)

				documents_req = request.POST['docs']
			
				user.schemes.append(scheme(name = name,description = description,
				category = category,
				gender = gender,
				Rate = Rate,
				education = education,
				overseas = overseas,
				income_ceiling = income_ceiling,
				disability = disability,
				documents_req = documents_req,
				sports = sports,
				org_name = user.name,
				org_id = user.id,
				field = field,
				tags=tags))
		
 				user.save()
 				#for obj in user.schemes:
 				#	print(obj.category)
				return HttpResponseRedirect('/organisations/add_remove/')
		return render(request,'organisations/add_scholarship.html',{'form':form})
	else:
		return HttpResponse('fuck off man')

def remove_scholarship(request):
	return HttpResponse(hello)


def logout(request):
	del request.session['mail']
	return HttpResponseRedirect('/organisations/')