from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from .serializers import ThingSerializer, RequestSerializer, ChatSerializer, TackleSerializer
from .models import Thing, Request, Chat, Tackle
from url_filter.integrations.drf import DjangoFilterBackend
from django.views.generic import TemplateView

def index(request):
    return render(request, 'days.html')

class ThingView(viewsets.ModelViewSet):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['name', 'date', 'points']

class RequestView(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['name', 'reporting_date']

class ChatView(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['name', 'reporting_date']

class TackleView(viewsets.ModelViewSet):
    queryset = Tackle.objects.all()
    serializer_class = TackleSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['name', 'reporting_date']

