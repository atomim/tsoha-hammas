# -*- coding: utf8 -*- 

from django.views.generic import TemplateView, DetailView, ListView
from utils import *
from tsohahammas.models import *

class MemberStatusMixin(object):
	def get_context_data(self, **kwargs):
		context = super(MemberStatusMixin, self).get_context_data(**kwargs)
		if super(MemberStatusMixin, self).get_object().members.get(pk=self.request.user.pk):
			context.update({'memberStatus': True})
		else:
			context.update({'memberStatus': False})
		return context

class GroupDetail(TitleMixin,MemberStatusMixin,DetailView): #this will change into listview when groups are done
	title='Ryhmän näytteet'
	template_name = 'group.html'
	model = Group


from django.conf.urls import patterns, include, url
group_patterns = patterns('',
    #url(r'^create/', login_required(CreateGroup.as_view()),name='groupCreate'),
    #url(r'^list/', GroupList.as_view(),name='groupList'),
    url(r'^(?P<pk>\d+)/', GroupDetail.as_view(),name='groupDetail'),
    url(r'^join/(?P<pk>\d+)/', GroupDetail.as_view(),name='joinGroup')
)

