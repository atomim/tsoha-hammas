from django.forms import ModelForm
from tsohahammas.models import *

class CreateSampleForm(ModelForm):
	class Meta():
		model=Sample
	#def __init__(self, *args, **kwargs):
	#	self.group = kwargs['initial']['group_id']
	#	return super(CreateGroupForm, self).__init__(*args, **kwargs)
	#def save(self, *args, **kwargs):
	#	obj = super(CreateSampleForm, self).save(False)
	#	obj.group = self.group
	#	if commit:
	#		obj.save()
	#	return obj
