from django.shortcuts import render

def base_temp(request):
	return render(request, 'portfolio/home.html')