from django.conf.urls import patterns, include, url
from tsohahammas.views import *
from django.views.generic import TemplateView
from class_based_auth_views.views import LoginView


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', index.Index.as_view(), name='index'),
    url(r'^group/',include(group.group_patterns)),
    url(r'^login/$', LoginView.as_view(template_name = 'login.html', success_url='/'), name='login'),
    url(r'^logout/','django.contrib.auth.views.logout',{'next_page': '/'},name='logout'),
    url(r'^admin/', include(admin.site.urls)),
)
