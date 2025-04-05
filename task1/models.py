from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import time

class SimpleModel(models.Model):
    title = models.CharField(max_length=100)

@receiver(post_save, sender=SimpleModel)
def after_save_signal(sender, instance, **kwargs):
    print("Signal started")
    time.sleep(5)
    print("Signal finished")
