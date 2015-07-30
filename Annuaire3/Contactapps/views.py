# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from Contactapps.models import User, Lieu, Contact
from django.utils import timezone
import random, sha, string

def index(request):
	
	#On demarre avec le traitement des informations concernants l'enregistrement d'un user
	
	#1. on se rassure que la requete qui arrive est de type POST
	
	if request.method == 'POST':

		#2. on va saler notre mot de passe puis on enregistrera notre nouvelle utilisateur
		password = request.POST['password']
		password_salt="".join([random.choice(string.letters) for i in range(8)])
		password_hash=sha.sha(password_salt + password).hexdigest()
	
		u = User(
			username = request.POST['username'],
			password_hash = password_hash,
			password_salt = password_salt,
			skypeid = request.POST['skypeid'],
			date_creation = timezone.now()		
		)
		
		u.save()

	return render_to_response("templates/index.html", context_instance=RequestContext(request))


def nouveaulieu(request):
	#on demarre avec l'enregistrement d'un nouveau lieu
	if request.method == 'POST':
		#on sauvegarde le tout dans notre base de donnees
		l = Lieu(
			pays = request.POST['pays'],
			region = request.POST['region'],
			ville = request.POST['ville']	
		)

		l.save()	
	
	return render_to_response("templates/lieu.html", context_instance=RequestContext(request))

def nouveaucontact(request):
	#on demarre avec l'enregistrement d'un nouveau lieu
	
	#1. on doit d'abord reccuperer toutes les lieux deja params dans la bd
	leslieux = Lieu.objects.all()	
	##. on prefixe l'utilisateur qui enregistre ses contacts car on a pas encore l'authentification
	currentuser =  User.objects.get(pk=1)
	if request.method == 'POST':
		#on reccupere au preablable le lieu selectionner
		l = Lieu.objects.get(pk=request.POST['lieu'])
		# on sauvegarde le nouveau contact beta dans notre base de donnee

		c = Contact(
			user = currentuser,
			lieu = l,
			names = request.POST['nom'],
			secondnames = request.POST['prenom'],
			birthday = request.POST['dateanniv'],
			date_creation = timezone.now()			
		)

		c.save()
			
	return render_to_response("templates/contact.html",{'leslieux':leslieux},context_instance=RequestContext(request))

