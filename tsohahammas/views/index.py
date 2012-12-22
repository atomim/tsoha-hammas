# -*- coding: utf8 -*- 

from django.views.generic import TemplateView, DetailView, ListView
from utils import *
from tsohahammas.models import *

class Index(TitleMixin,ListView): #this will change into listview when groups are done
	title='Julkiset ryhmät'
	template_name = 'index.html'
	queryset = Group.objects.all()

