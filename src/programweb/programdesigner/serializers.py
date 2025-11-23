from rest_framework import routers, serializers, viewsets
from .models import Speaker, Talk, Program, ProgramTalk, Event

# Serializers define the API representation.
class SpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speaker
        fields = '__all__' 


class TalkSerializer(serializers.ModelSerializer):
    speakers = SpeakerSerializer(many=True)
    class Meta:
        model = Talk
        fields = '__all__' 


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__' 

class ProgramSerializer(serializers.ModelSerializer):
    event = EventSerializer()
    talks = TalkSerializer(many=True)

    class Meta:
        model = Program
        fields = ['event', 'day', 'talks'] 

