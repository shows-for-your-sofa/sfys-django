from rest_framework import serializers

from .models import Event


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = [
            'date', 
            'start_time', 
            'end_time', 
            'name', 
            'event_link', 
            'contribution_link', 
            'description', 
            'artist', 
            'genre'
        ]
