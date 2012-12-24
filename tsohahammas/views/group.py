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
		obj=super(MemberStatusMixin, self).get_object()
		if obj.members.filter(pk=self.request.user.pk).count()==1:
			context.update({'is_member': True})
		else:
			context.update({'member': False})
		if obj.creator==self.request.user:
			context.update({'is_creator': True})
		else:
			context.update({'is_creator': False})
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

from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
patterns = patterns('',
    url(r'^create/', login_required(GroupCreate.as_view()),name='groupCreate'),
    #url(r'^list/', GroupList.as_view(),name='groupList'),
    url(r'^(?P<pk>\d+)/', GroupDetail.as_view(),name='groupDetail'),
    #url(r'^join/(?P<pk>\d+)/', GroupDetail.as_view(),name='joinGroup')
)

