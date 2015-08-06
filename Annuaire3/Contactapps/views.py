# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, loader, Context
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from Contactapps.models import Human, Lieu, Contact
from django.utils import timezone
from Contactapps.forms import ContactForm
import random, sha, string


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
		# quand l'on s'inscrit tout juste apres on est rediriger vers l'interface de connexion
		return HttpResponseRedirect(reverse(connexion))

	return render_to_response("templates/index.html", context_instance=RequestContext(request))



@login_required(redirect_field_name='rediriger_vers')
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


@login_required(redirect_field_name='rediriger_vers')
def nouvellepermission(request):
	currentuser =request
	#on demarre avec l'enregistrement d'un nouveau lieu
	if request.method == 'POST':
		#on sauvegarde le tout dans notre base de donnees
		content_type = ContentType.objects.get_for_model(Human)
		permission = Permission.objects.create(codename=request.POST['codename'],
                                       name=request.POST['name'],
                                       content_type=content_type)
		
		#une fois le lieu enregistrer on redirige vers la page de listing des lieux presents
		return HttpResponseRedirect(reverse('Contactapps.views.consoleadmin'))	
	
	return render_to_response("templates/permission.html",{'currentuser':currentuser},context_instance=RequestContext(request))



@login_required(redirect_field_name='rediriger_vers')
def gestionpermission(request):
	currentuser =request
	users = User.objects.all()
	permissions = Permission.objects.all()
	#on demarre avec l'enregistrement d'un nouveau lieu
	if request.method == 'POST':
		#on reccupere les infos de notre formulaire et on applique la permission sur notre utilisateur
		user = User.objects.get(pk=request.POST['idusername'])
		permission = Permission.objects.get(codename=request.POST['codename'])
		user.user_permissions.add(permission)
		#une fois le lieu enregistrer on redirige vers la page de listing des lieux presents
		return HttpResponseRedirect(reverse('Contactapps.views.gestionpermission'))	
	
	return render_to_response("templates/gestionpermission.html",{'currentuser':currentuser,'users':users,'permissions':permissions},context_instance=RequestContext(request))



@login_required(redirect_field_name='rediriger_vers')
def nouvellephoto(request, contact_id):
	context_instance=RequestContext(request)
	moncontact = Contact.objects.get(pk=contact_id)	
	if request.method == 'POST':	
		form = ContactForm(request.POST, request.FILES)	
		if form.is_valid():	
			moncontact.photo=form.cleaned_data['photo']
			moncontact.save()
		return HttpResponseRedirect(reverse('Contactapps.views.contacts'))	
	else:
		form = ContactForm()		
	
	return render_to_response('templates/detailinfocontact.html', {'moncontact': moncontact,'form':form},context_instance)


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
			human = Human.objects.get(pk=currentuser.user.human.id),
			lieu = l,
			names = request.POST['nom'],
			secondnames = request.POST['prenom'],
			birthday = request.POST['dateanniv'],
			date_creation = timezone.now()			
		)

		c.save()
		#une fois le lieu enregistrer on redirige vers la page de listing des contacts
		return HttpResponseRedirect(reverse('Contactapps.views.contacts'))	
			
	return render_to_response("templates/contact.html",{'leslieux':leslieux,'currentuser':currentuser},context_instance=RequestContext(request))



@login_required(login_url='/connexion/',redirect_field_name='rediriger_vers')
def contacts(request):	
	
	##. on reccupere les informations de l'utilisateur courant
	currentuser =request			
	mescontacts = Contact.objects.filter(human=currentuser.user.human.id)	
	nombredecontact = mescontacts.count()
	return render_to_response("templates/listecontact.html",{'nombredecontact':nombredecontact,'mescontacts':mescontacts,'currentuser': currentuser},context_instance=RequestContext(request))



@login_required(login_url='/connexion/',redirect_field_name='rediriger_vers')
def lieux(request):	
	
	#1. on liste tous les lieux 
	leslieux = Lieu.objects.all()	
	currentuser =request
	
	t = loader.get_template("templates/listelieux.html")
	
	return render_to_response("templates/listelieux.html",{'currentuser':currentuser,'leslieux': leslieux},context_instance=RequestContext(request))

		

@login_required(login_url='/connexion/',redirect_field_name='rediriger_vers')
def consoleadmin(request):	
	
	#1. on reccupere l'utilisateur courant
	currentuser =request	
	return render_to_response("templates/consoleadmin.html",{'currentuser':currentuser},context_instance=RequestContext(request))


@login_required(redirect_field_name='rediriger_vers')
def users(request):	
	
	#1. on liste tous les lieux 
	utilisateurs = Human.objects.all()		
	return render_to_response("templates/listedesutilisateurs.html",{'utilisateurs':utilisateurs})


@login_required(redirect_field_name='rediriger_vers')
def detailinfocontact(request,contact_id):	
	form = ContactForm()
	#1. on liste tous les lieux 
	moncontact = Contact.objects.get(pk=contact_id)	
	#1. on reccupere l'utilisateur courant
	currentuser =request	
	context_instance=RequestContext(request)
	return render_to_response("templates/detailinfocontact.html",{'form':form,'moncontact':moncontact,'currentuser':currentuser},context_instance)

@login_required(redirect_field_name='rediriger_vers')
def supprimercontact(request,contact_id):	
	
	#1. on supprime le contact
	moncontact = Contact.objects.get(pk=contact_id)	
	moncontact.delete()
	return HttpResponseRedirect(reverse('Contactapps.views.contacts'))
	
@login_required(redirect_field_name='rediriger_vers')
def supprimeruser(request,human_id):	
	
	#1. on liste tous les lieux 
	human = Human.objects.get(pk=human_id)
	
	#on supprime aussi ces contacts
	mescontacts = Contact.objects.filter(human=human_id)
	mescontacts.delete()
	human.delete()	
	return HttpResponseRedirect(reverse('Contactapps.views.users'))


def connexion(request):	
	
	if request.method == 'POST':	
		username = request.POST['username']
	   	password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('Contactapps.views.contacts'))	
			else:
				return HttpResponse('votre compte a ete desactive')
		else:
			return HttpResponse('Login ou mot de passe incorrecte')			
			
	return render_to_response("templates/connexion.html",context_instance=RequestContext(request))



def deconnexion(request):
	logout(request)
	return HttpResponseRedirect(reverse(connexion))


