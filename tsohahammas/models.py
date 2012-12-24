from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from cuser.fields import CurrentUserField

class Group(models.Model):
     name = models.CharField(max_length=100)
     description = models.TextField()
     hidden = models.BooleanField()
     date_created= models.DateTimeField(auto_now_add=True)
     creator = CurrentUserField(add_only=True)
     members = models.ManyToManyField(User,related_name='r_groups')
     def get_absolute_url(self):
    	return reverse('groupDetail', args=[str(self.id)])
     def __unicode__(self):
        return self.name

class Sample(models.Model):
     sample_id= models.AutoField(primary_key=True)
     date_added= models.DateTimeField(auto_now_add=True)
     picture = models.ImageField(upload_to="images/")
     adder = CurrentUserField(add_only=True)
     group = models.ForeignKey(Group)
     def get_absolute_url(self):
    	return reverse('sampleDetail', args=[str(self.sample_id)])
