# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from Contactapps.models import User, Lieu
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

