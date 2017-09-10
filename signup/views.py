from django.shortcuts import render
from django.http import HttpResponse

def stu_signup(request):
	#return HttpResponse("hello")
	return render(request,'signup/stu_signup.html')

def org_signup(request):
	return render(request,'signup/org_signup.html')