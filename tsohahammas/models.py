from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
     name = models.CharField(max_length=100)
     description = models.TextField()
     hidden = models.BooleanField()
     date_created= models.DateTimeField()
     creator = models.ForeignKey(User)
     members = models.ManyToManyField(User,related_name='r_groups')
     def __unicode__(self):
        return self.name

class Sample(models.Model):
     sample_id= models.AutoField(primary_key=True)
     date_added= models.DateTimeField()
     picture = models.ImageField(upload_to="images/")
     adder = models.ForeignKey(User)
     group = models.ForeignKey(Group)
     
