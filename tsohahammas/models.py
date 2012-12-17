from django.db import models

def Group(models.Model):
     name = models.CharField(max_length=100)
     description = models.TextField()
     hidden = models.BooleanField()
     date_created= models.DateTimeField()
     creator = models.ForeignKey('User')
     members = models.ManyToManyField('User')
     def __unicode__(self):
        return self.name

def Sample(models.Model):
     sample_id= models.AutoField()
     date_added= models.DateTimeField()
     picture = models.ImageField()
     adder = models.ForeignKey('User')
     group = models.ForeignKey('Group')
     

