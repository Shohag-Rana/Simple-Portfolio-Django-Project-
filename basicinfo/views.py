from django.shortcuts import render

# Create your views here.
def contact(request):
	return render(request, 'basicinfo/contact.html')

def service(request):
	return render(request, 'basicinfo/service.html')

def skill(request):
	return render(request, 'basicinfo/skill.html')