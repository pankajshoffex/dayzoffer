from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Country(models.Model):
	title = models.CharField(max_length=120, unique=True)
	active = models.BooleanField(default=True)
	
	def __unicode__(self):
		return self.title

class State(models.Model):
	country = models.ForeignKey(Country)
	title = models.CharField(max_length=120, unique=True)
	active = models.BooleanField(default=True)

	def __unicode__(self):
		return self.title

class City(models.Model):
	country = models.ForeignKey(Country)
	state = models.ForeignKey(State, blank=True)
	title = models.CharField(max_length=120, unique=True)
	active = models.BooleanField(default=True)
	
	def __unicode__(self):
		return self.title

class SellerUser(models.Model):
	user = models.OneToOneField(User)
	firm_name = models.CharField(max_length=120)
	address = models.TextField()
	location_aria = models.CharField(max_length=120)
	country = models.ForeignKey(Country)
	state = models.ForeignKey(State)
	city = models.ForeignKey(City)
	pincode = models.CharField(max_length=10)
	lattitude = models.CharField(max_length=120, blank=True, null=True)
	longitute = models.CharField(max_length=120, blank=True, null=True)
	mobile = models.CharField(max_length=120)

	def __unicode__(self):
		return self.user.username

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	city = models.ForeignKey(City)
	location_aria = models.CharField(max_length=120)
	mobile_no = models.CharField(max_length=20)

	def __unicode__(self):
		return self.user.username




