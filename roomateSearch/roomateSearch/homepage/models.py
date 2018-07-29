from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.crypto import get_random_string
import uuid


# Create your models here.

class RoomateUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    answer_one = models.CharField(max_length=30)
    answer_two = models.CharField(max_length=30)
    answer_three = models.CharField(max_length=30)
    answer_four = models.CharField(max_length=30)
    answer_five = models.CharField(max_length=30)
    bio = models.CharField(max_length=500)
    picturepath = get_random_string(length=16) + str(uuid.uuid4())
    picture = models.ImageField(upload_to=picturepath, null = True)
    messages = []
    
    #citation: code to help update the models properly when instances are created/saved
    #https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
    @receiver(post_save, sender=User)
    def create_user_roomateuser(sender, instance, created, **kwargs):
        if created:
            RoomateUser.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_roomateuser(sender, instance, **kwargs):
        instance.roomateuser.save()
    #citation done
    