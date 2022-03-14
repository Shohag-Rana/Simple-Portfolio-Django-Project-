from django.db import models

# Create your models here
STATE_CHOICES = (
    ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'),
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Assam', 'Assam'),
    ('Dhaka', 'Dhaka'),
    ('Rajshahi', 'Rajshahi'),
    ('Comilla', 'Comilla'),
    ('Rangpur', 'Rangpur'),
    ('Thakurgaon', 'Thakurgaon'),
)

class Student(models.Model):
	stu_id = models.IntegerField()
	name = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	zipcode = models.IntegerField()
	state = models.CharField(choices=STATE_CHOICES, max_length=50)

	def __str__(self):
		return self.name



