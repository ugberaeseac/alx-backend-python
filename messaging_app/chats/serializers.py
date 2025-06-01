#!/usr/bin/python3

"""

"""

from rest_framework import serializers
from .models import User, Conversation, Message


class UserSerializer(serializers.ModelSerializer):
    """ serialize the User class """

    class Meta:
        model = User
        fields = '__all__'


class ConversationSerializer(serializers.ModelSerializer):
    """ serialize the Conversation class """
    participants = UserSerializer(Many=True, read_only=True)
    messages = MessageSerializer(Many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = '__all__'


class MessageSerializer(serializer.ModelSerializer):
    """ serialize the Message class """
    sender = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = '__all__'
