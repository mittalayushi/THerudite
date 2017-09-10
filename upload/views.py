from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from models import User,Scholarship		

def upload(request):
	if request.method == 'POST':
		if request.is_ajax():
			image = request.POST.get('image')
			id_token=request.POST.get('id_token')
		 	emailx = request.POST.get('email')
		 	name=request.POST.get('name')
		 	print(9)
		 	try:
		 		user = User.objects.get(email=emailx)
		 		request.session['mail']=emailx
		 		print(request.session['mail'])
		 		print(1)

		 	except User.DoesNotExist:
		 		user = User.objects.create(
		 			name=name,
		 			image=image,
		 			email=emailx,
		 			id_token=id_token)
		 		user.save()
		 		request.session['mail']=emailx
		 		print(request.session['mail'])
		 		print(0)
		 	finally:
		 		print(99)
		 		request.session.save()

		 		return HttpResponse(user)
def resume(request):
	if request.session.has_key('mail'):
		emailx = request.session['mail']
		user = User.objects.get(email=emailx)
		name=user.name
		#print(name)
		#print("ekta")
		#print(emailx)
		#print("varshney")
		return render(request,'upload/upload.html',{"mail":emailx,"name":name})
	else:
		return HttpResponseNotFound("You are smart.. You know what to do before having access to this site ;)")


def fill_details(request):
	if request.session.has_key('mail'):
		emailx = request.session['mail']
		user = User.objects.get(email=emailx)
		name=user.name
		return render(request,'upload/form.html',{"mail":emailx,"name":name})
	else:
		return HttpResponseNotFound("You are a smart ass.. You know what to do before you can access anything! ;)")

