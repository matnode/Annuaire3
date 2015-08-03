# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.models import User
from Contactapps.models import Human, Lieu, Contact
from django.utils import timezone
import random, sha, string

@login_required(redirect_field_name='rediriger_vers')
def index(request):	
	#On demarre avec le traitement des informations concernants l'enregistrement d'un user
	
	#1. on se rassure que la requete qui arrive est de type POST
	
	if request.method == 'POST':
		#2. on va saler notre mot de passe puis on enregistrera notre nouvelle utilisateur
		user = User.objects.create_user(
			username = request.POST['username'],
			email = request.POST['email'],
			password = request.POST['password']
		)		
	
		h = Human(
			user = user,
			online =0,			
			skypeid = request.POST['skypeid'],	
		)
		
		h.save()

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
		#une fois le lieu enregistrer on redirige vers la page de listing des lieux presents
		return HttpResponseRedirect(reverse('Contactapps.views.lieux'))	
	
	return render_to_response("templates/lieu.html", context_instance=RequestContext(request))


@login_required(login_url='/connexion/',redirect_field_name='rediriger_vers')
def nouveaucontact(request):
	#on demarre avec l'enregistrement d'un nouveau lieu
	
	#1. on doit d'abord reccuperer toutes les lieux deja params dans la bd
	leslieux = Lieu.objects.all()	
	##. on reccupere les informations de l'utilisateur courant
	currentuser =request	
	if request.method == 'POST':
		#on reccupere au preablable le lieu selectionner
		l = Lieu.objects.get(pk=request.POST['lieu'])
		# on sauvegarde le nouveau contact beta dans notre base de donnee

		c = Contact(
			human = currentuser,
			lieu = l,
			names = request.POST['nom'],
			secondnames = request.POST['prenom'],
			birthday = request.POST['dateanniv'],
			date_creation = timezone.now()			
		)

		c.save()
			
	return render_to_response("templates/contact.html",{'leslieux':leslieux},context_instance=RequestContext(request))

@login_required(login_url='/connexion/',redirect_field_name='rediriger_vers')
def contacts(request):	
	
	##. on reccupere les informations de l'utilisateur courant
	currentuser =request			
	mescontacts = Contact.objects.filter(human=currentuser)		
	return render_to_response("templates/listecontact.html",{'mescontacts':mescontacts,'currentuser': currentuser},context_instance=RequestContext(request))


@login_required(login_url='/connexion/',redirect_field_name='rediriger_vers')
def lieux(request):	
	
	#1. on liste tous les lieux 
	leslieux = Lieu.objects.all()	
	currentuser =request	
	return render_to_response("templates/listelieux.html",{'leslieux':leslieux,'currentuser':currentuser})


def users(request):	
	
	#1. on liste tous les lieux 
	utilisateurs = Human.objects.all()		
	return render_to_response("templates/listedesutilisateurs.html",{'utilisateurs':utilisateurs})


def connexion(request):	
	
	if request.method == 'POST':	
		username = request.POST['username']
	   	password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('Contactapps.views.users'))	
			else:
				return HttpResponse('votre compte a ete desactive')
		else:
			return HttpResponse('Login ou mot de passe incorrecte')			
			
	return render_to_response("templates/connexion.html",context_instance=RequestContext(request))


def deconnexion(request):
	logout(request)
	return HttpResponseRedirect(reverse(connexion))


