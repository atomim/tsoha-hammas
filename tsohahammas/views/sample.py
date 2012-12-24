# -*- coding: utf8 -*- 

from django.views.generic import TemplateView, DetailView, ListView, edit
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

from tsohahammas.forms import *
class SampleCreate(edit.CreateView):
	model = Sample
	template_name = 'form.html'
	#def get_initial(self):
	#	print self.kwargs['group_id']
	#	super(SampleCreate,self).get_initial()
	#	self.initial.update({ 'group': self.kwargs['group_id'] })
	#	return self.initial
	

from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
patterns = patterns('',
    url(r'^create/(?P<group_id>\d+)/', login_required(SampleCreate.as_view()),name='sampleCreate'),
    #url(r'^list/', GroupList.as_view(),name='groupList'),
    url(r'^(?P<pk>\d+)/', SampleDetail.as_view(),name='sampleDetail')
)

