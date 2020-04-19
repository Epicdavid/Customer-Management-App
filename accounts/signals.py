from django.dispatch import receiver 
from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from .models import *


@receiver(post_save,sender=User)
def customer_g(sender, instance, created, **kwargs):
    if Group.objects.filter(name='Customer'):
        group = Group.objects.get(name='Customer')
        if created:
            instance.groups.add(group)
            Customer.objects.create(user=instance, name=instance.username, email=instance.email)

