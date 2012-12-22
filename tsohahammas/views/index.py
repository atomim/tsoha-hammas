# -*- coding: utf8 -*- 

from django.views.generic import ListView
from utils import *
from tsohahammas.models import *

class Index(TitleMixin,ListView):
	title='Julkiset ryhmät'
	template_name = 'index.html'
	queryset = Group.objects.all()

