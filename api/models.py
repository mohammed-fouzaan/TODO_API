from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200,null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    progress = models.CharField(max_length=200,default='To Do', editable=True)
    priority = models.CharField(max_length=200,null=True, blank=True)
    duedate = models.CharField(max_length=200,null=True, blank=True)
    created = models.CharField(max_length=200,default= datetime.now().strftime("%d/%m/%Y %H:%M:%S"), editable=False)
    edited = models.CharField(max_length=200,default='Task wasn\'t updated since it\'s creation', editable=True)

def __str__(self):
        return self.title
class Meta:
        order_with_respect_to = 'user'