import threading
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
import logging


logging.basicConfig(level=logging.INFO)

@receiver(post_save, sender=User)
def signal_handler(sender, instance, created, **kwargs):
    if created:
        logging.info(f"Signal handler running in thread: {threading.current_thread().name}")
        logging.info(f"User {instance.username} created!")
