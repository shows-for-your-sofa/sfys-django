from django.views.generic.base import TemplateView
from rest_framework import permissions, viewsets

from .models import Event
from .serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]


class EventsView(TemplateView):
    template_name = "events.html"


    
