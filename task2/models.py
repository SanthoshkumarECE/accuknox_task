import threading
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class ThreadModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=ThreadModel)
def check_thread(sender, instance, **kwargs):
    print(f"Signal thread ID: {threading.get_ident()}")
