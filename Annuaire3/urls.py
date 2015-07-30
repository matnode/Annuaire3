from django.conf.urls.defaults import patterns, include, url

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
    url(r'^user/$', 'Contactapps.views.index'),
    url(r'^user/nouveaulieu/$', 'Contactapps.views.nouveaulieu')
    url(r'^user/nouveaucontact/$', 'Contactapps.views.nouveaucontact')
)
