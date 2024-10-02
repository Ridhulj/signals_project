from django.contrib.auth.models import User
from django.http import HttpResponse
import threading
import logging

logging.basicConfig(level=logging.INFO)


def create_user(request):
    logging.info(f"View running in thread: {threading.current_thread().name}")

    username = 'test_user'  # Change this to test for uniqueness
    user = User.objects.create_user(username=username, password='testpassword123')

    return HttpResponse(f"User {username} created successfully!")
