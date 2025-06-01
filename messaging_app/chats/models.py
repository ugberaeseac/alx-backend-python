from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

# Create your models here.

class User(AbstractUser):
    """ """
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return 'User ({}, {}, {})'.format(self.id, self.username, self.email)


class Conversation(models.Model):
    """ """
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='conversations')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Conversation ({})'.format(self.id)


class Message(models.Model):
    """ """
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_messages')
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Message ({} - {})'.format(self.sender.username, self.content[:30])
