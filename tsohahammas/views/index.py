from django.views.generic import TemplateView, DetailView, ListView


class Index(TemplateView): #this will change into listview when groups are done
     template_name = 'index.html'

