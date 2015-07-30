from django.db import models
import sha
# Create your models here.

class User(models.Model):
	username = models.CharField(max_length=255)
	skypeid = models.CharField(max_length=255) 
	password_salt = models.CharField(max_length=8, null=True)
	password_hash = models.CharField(max_length=40, null=True)
	date_creation = models.DateTimeField()
	
	def __unicode__(self):
		return self.username
	

class Contact(models.Model):
	names = models.TextField()
	secondnames = models.TextField()
	birthday = models.DateTimeField()
	date_creation = models.DateTimeField()

	def __unicode__(self):
		return self.names
	def __unicode__(self):
		return self.secondnames

class Lieu(models.Model):
	pays = models.CharField(max_length=255)
	region = models.CharField(max_length=255)
	ville = models.CharField(max_length=255)

	def __unicode__(self):
		return self.pays
	def __unicode__(self):
		return self.region
	def __unicode__(self):
		return self.ville
