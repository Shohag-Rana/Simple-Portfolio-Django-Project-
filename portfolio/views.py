from django.shortcuts import render
from . models import Student
from . forms import StudentRegistration, Registration

# Create your views here.
def home(request):
	stuall = Student.objects.filter(pk = 2)
	print(stuall)
	return render(request, 'portfolio/home.html',{'stuall': stuall})

def form_test(request):
	if request.method == "POST":
		fm = Registration(request.POST)
		if fm.is_valid():
			nm = fm.cleaned_data['name']
			mail = fm.cleaned_data['email']
			home = fm.cleaned_data['village']
			print(nm, mail, home)
			print('this is post request')
			fm = Registration()
		else:
			print('form data is not valid')
	else:
		print('this is get request')
		fm = Registration() 
		fm.order_fields(field_order=['name', 'email', 'village'])
	return render(request, 'portfolio/form.html', {'form': fm})