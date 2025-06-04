#!/usr/bin/python3

"""

"""

from rest_framework import serializers
from .models import User, Conversation, Message


class UserSerializer(serializers.ModelSerializer):
    """ serialize the User class """

    class Meta:
        model = User
        fields = (
                'user_id',
                'first_name',
                'last_name',
                'phone_number',
            )



class MessageSerializer(serializers.ModelSerializer):
    """ serialize the Message class """

    class Meta:
        model = Message
        fields = (
                'message_id',
                'sender',
                'conversation',
                'message_body',
                'sent_at',
                'created_at'
            )

    def validate_msgbody(self, value):
        if len(message_body) == 0:
            raise serializers.ValidationError(
                    'You cannot send an empty message'
                    )
        return value


class ConversationSerializer(serializers.ModelSerializer):
    """ serialize the Conversation class """

    messages = MessageSerializer(many=True, read_only=True)
    total_messages = serializers.SerializerMethodField()

    def get_total_messages(self, obj):
        count = 0
        msgs = obj.messages.all()
        for msg in msgs:
            count += 1
        return count


    class Meta:
        model = Conversation
        fields = (
                'partipants',
                'created_at',
                'total_messages',
            )
