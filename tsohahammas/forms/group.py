from django.forms import ModelForm
from tsohahammas.models import *

class CreateGroupForm(ModelForm):
	class Meta():
		model=Group


from django.contrib import admin
class GroupAdmin(admin.ModelAdmin):
	form=CreateGroupForm

