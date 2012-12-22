# -*- coding: utf8 -*- 

from django.views.generic import TemplateView, DetailView, ListView
from utils import *
from tsohahammas.models import *

class OwnerMixin(object):
	def get_context_data(self, **kwargs):
		context = super(OwnerMixin, self).get_context_data(**kwargs)
		if super(OwnerMixin, self).get_object().adder==self.request.user:
			context.update({'owner': True})
		else:
			context.update({'owner': False})
		return context

class SampleDetail(TitleMixin,OwnerMixin,DetailView): 
	title='Näyte'
	template_name = 'sample.html'
	model = Sample
	

from django.conf.urls import patterns, include, url
patterns = patterns('',
    #url(r'^create/', login_required(CreateGroup.as_view()),name='groupCreate'),
    #url(r'^list/', GroupList.as_view(),name='groupList'),
    url(r'^(?P<pk>\d+)/', SampleDetail.as_view(),name='sampleDetail')
)

