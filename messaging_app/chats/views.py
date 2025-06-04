from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from .models import User, Conversation, Message
from .serializers import MessageSerializer


# Create your views here.

@api_view(['GET'])
def home(request):
    """ """
    return HttpResponse('<h1>Home Page</h1>')





@api_view(['GET'])
def conversation_list(request):
    """ list all conversations """
    conv = Conversation.objects.all()
    serializer = MessageSerializer(conv, many=True)
    return Response(serializer.data)
