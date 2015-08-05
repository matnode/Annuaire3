from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Human(models.Model):
	user = models.OneToOneField(User)
	skypeid = models.CharField(max_length=255) 
	online = models.CharField(max_length=1)	
	
	def __unicode__(self):
		return self.skypeid
	def __unicode__(self):
		return self.online


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
	class Meta:
		permissions = (
			("ajouter_lieu","ajouter un lieu"),
	)


class Contact(models.Model):
	human = models.ForeignKey(Human)
	lieu = models.ForeignKey(Lieu) 
	names = models.TextField()
	secondnames = models.TextField()
	birthday = models.TextField()
	date_creation = models.DateTimeField()
	photo = models.ImageField(upload_to="photos/")

	def __unicode__(self):
		return self.names
	def __unicode__(self):
		return self.secondnames

