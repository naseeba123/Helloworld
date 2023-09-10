from django.db import models

class register(models.Model):
	name=models.CharField(max_length=100)
	phone=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	password=models.CharField(max_length=100)
	usertype=models.CharField(max_length=100,default='user')
	status=models.CharField(max_length=100,default='pending')


class add(models.Model):
	book=models.CharField(max_length=100)
	author=models.CharField(max_length=100)
	date=models.CharField(max_length=100)
	edition=models.CharField(max_length=100)
	pages=models.CharField(max_length=100)
	copies=models.CharField(max_length=100)
	description=models.CharField(max_length=100)
	image=models.ImageField(upload_to='images')

class requst(models.Model):
	rr=models.ForeignKey(register,on_delete=models.CASCADE)
	aa=models.ForeignKey(add,on_delete=models.CASCADE)
	status=models.CharField(max_length=100)
	z=models.CharField(max_length=100)
		
# Create your models here.
