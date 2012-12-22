# -*- coding: utf8 -*- 

from django.views.generic import TemplateView, DetailView, ListView
from utils import *

class Index(TitleMixin,TemplateView): #this will change into listview when groups are done
	title='Julkiset ryhmät'
	template_name = 'index.html'

