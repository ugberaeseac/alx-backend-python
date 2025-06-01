from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
import uuid

# Create your models here.

class User(AbstractUser):
    """ """
    user_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    password = models.CharField(max_length=128, blank=False, null=False)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    
    def __str__(self):
        return 'User ({}, {}, {})'.format(self.id, self.username, self.email)


class Conversation(models.Model):
    """ """
    conversation_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='conversations')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Conversation ({})'.format(self.id)


class Message(models.Model):
    """ """
    message_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_messages')
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    message_body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Message ({} - {})'.format(self.sender.username, self.content[:30])
