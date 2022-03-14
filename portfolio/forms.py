from django import forms

class StudentRegistration(forms.Form):
	email = forms.EmailField()
	hometown = forms.CharField()
	name = forms.CharField()

	 
class Registration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    village = forms.CharField()
    password = forms.CharField()