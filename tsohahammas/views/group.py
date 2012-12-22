# -*- coding: utf8 -*- 

from django.views.generic import TemplateView, DetailView, ListView
from utils import *
from tsohahammas.models import *


class GroupDetail(TitleMixin,DetailView): #this will change into listview when groups are done
	title='Ryhmän näytteet'
	template_name = 'group.html'
	model = Group


from django.conf.urls import patterns, include, url
group_patterns = patterns('',
    #url(r'^create/', login_required(CreateGroup.as_view()),name='groupCreate'),
    #url(r'^list/', GroupList.as_view(),name='groupList'),
    url(r'^(?P<pk>\d+)/', GroupDetail.as_view(),name='groupDetail')
)

