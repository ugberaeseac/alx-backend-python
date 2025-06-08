from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import viewsets, status, filters
from django.http import HttpResponse
from .models import User, Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer
from .permissions import IsParticipantOfConversation


# Create your views here.

@api_view(['GET'])
def home(request):
    """ """
    return HttpResponse('<h1>Home Page</h1>')


class ConversationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsParticipantOfConversation]
    serializer_class = ConversationSerializer

    def get_queryset(self):
        return Conversation.objects.filter(participants=self.request.user)


class MessageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = MessageSerializer

    def get_queryset(self):
        return Message.objects.filter(conversation__particpants=self.request.user)

    def perform_create(self, serializer):
        conversation = serializer.validate_data.get('conversation')
        if self.request.user not in conversation__participants.all():
            raise PermissionDenied('You can not send a message to this conversation')
        serializer.save(sender=self.request.user)

    def perform_update(self, serializer):
        conversation = serializer.instance.conversation
        if self.request.user not in conversation__participants.all():
            raise PermissionDenied('You are not a participant in this conversation')
        serializer.save()

    def perform_delete(self, instance):
        conversation = instance.conversation
        if self.request.user not in conversation__participants.all():
            raise PermissionDenied('You are not a participant in this conversation')
        instance.delete()


