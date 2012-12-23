from tsohahammas.models import *
from tsohahammas.forms import *
from django.contrib import admin

admin.site.register(Group,group.GroupAdmin)
admin.site.register(Sample)
