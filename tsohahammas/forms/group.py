from django.forms import ModelForm
from tsohahammas.models import *

class CreateGroupForm(ModelForm):
	class Meta():
		model=Group
	def __init__(self, *args, **kwargs):
		self.creator = kwargs['initial']['creator']
		return super(CreateGroupForm, self).__init__(*args, **kwargs)
	def save(self, *args, **kwargs):
		obj = super(CreateGroupForm, self).save(False)
		obj.creator = self.creator
		if commit:
			obj.save()
		return obj

from django.contrib import admin
class GroupAdmin(admin.ModelAdmin):
	form=CreateGroupForm
