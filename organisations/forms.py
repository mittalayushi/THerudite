from django import forms
from django.forms import ModelForm
#from org_login.models import loginModel
#from org_login.models import signupModel
from organisations.models import org

class loginForm(forms.Form):
	class Meta:
		model = org

class signupForm(forms.Form):
	class Meta:
		model = org

class NewScholarshipForm(forms.Form):
	class Meta:
		model = org