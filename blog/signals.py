from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post
import threading


@receiver(post_save, sender=Post)
def post_saved_handler(sender, instance, created, **kwargs):
    print(f"Post saved! Title: {instance.title}")
    print(f"Is this happening in a new thread? {threading.current_thread()}")
