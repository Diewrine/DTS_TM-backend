from django.db import models
from django.contrib.auth.models import User

# Create your models here.


"""
class User(models.Model):
	username = models.CharField(max_length=120)
	password = models.CharField(max_length=50)

	def __str__(self):
		return self.username
"""


class Member(models.Model):
	"""docstring for Member"""
	owner = models.ForeignKey(User, related_name="member",on_delete=models.SET_NULL,null=True)
	firstname = models.CharField(max_length=120)
	lastname = models.CharField(max_length=120)
	address = models.CharField(max_length=120)
	phone = models.IntegerField()
	updated_at = models.DateField(auto_now=True)

	def __str__(self):
		return self.firstname
		