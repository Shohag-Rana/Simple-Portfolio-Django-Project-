from django.urls import path
from . import views

urlpatterns = [
	path('contact/', views.contact, name = 'contact'),
	path('service/', views.service, name = 'service'),
	path('skill/', views.skill, name = 'skill'),
]