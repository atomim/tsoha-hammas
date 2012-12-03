from django.conf.urls import patterns, include, url
from tsohahammas.views import *
from django.views.generic import TemplateView


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tsohahammas.views.home', name='home'),
    # url(r'^tsohahammas/', include('tsohahammas.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    
    #url(r'^login/', LoginView.asView()),
    url(r'^(index.html|)', TemplateView.as_view(template_name='index.html')),
    url(r'^admin/', include(admin.site.urls)),
)
