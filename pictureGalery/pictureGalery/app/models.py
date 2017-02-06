"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User, UserManager
from django.core.validators import MaxLengthValidator

# Create your models here.
class CastomUser(User):
	telephone = models.CharField(max_length = 13)
	objects = UserManager()


class Picture(models.Model):
	id = models.IntegerField( primary_key = True)
	cost = models.DecimalField(max_digits=10, decimal_places=2)
	stile = models.CharField(max_length = 30)
	date = models.DateField()

class Card(models.Model):
	customer  = models.ForeignKey(CastomUser,on_delete=models.CASCADE)
	product = models.ForeignKey(Picture,on_delete=models.CASCADE)
	date_added = models.DateTimeField(auto_now_add=True)

class Messages(models.Model):
	name = models.CharField(max_length = 30)
	email = models.EmailField(max_length=70,blank=True)
	massage = models.TextField(validators=[MaxLengthValidator(200)])
	date_added = models.DateTimeField(auto_now_add=True)