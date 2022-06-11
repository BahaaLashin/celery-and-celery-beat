from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Book(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    publish_date = models.DateField( auto_now=False, auto_now_add=False)
    auther_name = models.CharField( max_length=50)
    
@receiver(pre_save,sender=Book)
def notify(sender,instance,**kwargs):
    print(sender.objects)
    print(instance.name)
    print(kwargs)