from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from django.http import HttpResponse
from .models import User, Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer


# Create your views here.

@api_view(['GET'])
def home(request):
    """ """
    return HttpResponse('<h1>Home Page</h1>')


class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
