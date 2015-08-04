from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Annuaire3.views.home', name='home'),
    # url(r'^Annuaire3/', include('Annuaire3.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls))
    # url utiliser pour l'insertion des donnees(utilisateur, lieu et contact)
    url(r'^user/$', 'Contactapps.views.index'),
    url(r'^user/nouveaulieu/$', 'Contactapps.views.nouveaulieu'),
    url(r'^user/nouveaucontact/$', 'Contactapps.views.nouveaucontact'),
    url(r'^user/(?P<contact_id>\d+)/nouvellephoto/$', 'Contactapps.views.nouvellephoto'),
    #url utiliser pour le listing des donnees (utilisateur, lieu et contact)
    url(r'^user/contact/$', 'Contactapps.views.contacts'),
    url(r'^user/(?P<contact_id>\d+)/detail/$', 'Contactapps.views.detailinfocontact'),
    url(r'^user/lieu/$', 'Contactapps.views.lieux'),    
    url(r'^user/listedesutilisateurs/$', 'Contactapps.views.users'),
    url(r'^user/consoledadministration/$', 'Contactapps.views.consoleadmin'),
    url(r'^connexion/$', 'Contactapps.views.connexion'),
    url(r'deconnexion/$', 'Contactapps.views.deconnexion'),
)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
