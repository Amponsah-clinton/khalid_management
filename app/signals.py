# yourapp/signals.py
from django.contrib.auth.models import User
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def create_users(sender, **kwargs):
    # Check if the users already exist, if not create them
    if not User.objects.filter(username='khalid1@gmail.com').exists():
        User.objects.create_user(username='khalid1@gmail.com', email='khalid1@gmail.com', password='Khalid12025180')
    if not User.objects.filter(username='khalid2@gmail.com').exists():
        User.objects.create_user(username='khalid2@gmail.com', email='khalid2@gmail.com', password='Khalid22025360')
