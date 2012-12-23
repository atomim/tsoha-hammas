# -*- coding: utf8 -*- 

from django.views.generic import TemplateView, DetailView, ListView, edit
from utils import *
from tsohahammas.models import *

class GroupSamplesMixin(object):
	def get_context_data(self, **kwargs):
		context = super(GroupSamplesMixin, self).get_context_data(**kwargs)
		context.update({'samples': super(MemberStatusMixin, self).get_object().sample_set.all()})
		return context

class MemberStatusMixin(object):
	def get_context_data(self, **kwargs):
		context = super(MemberStatusMixin, self).get_context_data(**kwargs)
		if super(MemberStatusMixin, self).get_object().members.get(pk=self.request.user.pk):
			context.update({'memberStatus': True})
		else:
			context.update({'memberStatus': False})
		return context

class GroupDetail(GroupSamplesMixin,TitleMixin,MemberStatusMixin,DetailView):
	title = 'Ryhmän näytteet'
	template_name = 'group.html'
	model = Group
	

from tsohahammas.forms import *
from django.core.urlresolvers import reverse
class GroupCreate(edit.CreateView):
	model = Group
	template_name = 'form.html'
	form_class=group.CreateGroupForm
	def get_initial(self):
		self.initial.update({ 'creator': self.request.user })
		return self.initial

from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
patterns = patterns('',
    url(r'^create/', login_required(GroupCreate.as_view()),name='groupCreate'),
    #url(r'^list/', GroupList.as_view(),name='groupList'),
    url(r'^(?P<pk>\d+)/', GroupDetail.as_view(),name='groupDetail'),
    #url(r'^join/(?P<pk>\d+)/', GroupDetail.as_view(),name='joinGroup')
)

