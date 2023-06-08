from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class ChatRoom(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

class Message(models.Model):
    room=models.ForeignKey(ChatRoom, related_name='messages',on_delete=models.CASCADE)
    user=models.ForeignKey(User, related_name='messages',on_delete=models.CASCADE)
    content = models.TextField()
    data_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('data_added',)

