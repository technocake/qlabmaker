from rest_framework import routers, serializers, viewsets
from .models import Speaker, Host, Talk, Program, ProgramTalk, Event, Person


# Serializers define the API representation.
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__' 


class SpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speaker
        fields = '__all__' 

class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = '__all__' 


class TalkSerializer(serializers.ModelSerializer):
    speakers = SpeakerSerializer(many=True)
    class Meta:
        model = Talk
        fields = '__all__' 


class EventSerializer(serializers.ModelSerializer):
    year = serializers.SerializerMethodField()

    def get_year(self, obj):
        return obj.year()

    class Meta:
        model = Event
        fields = '__all__' 

class ProgramSerializer(serializers.ModelSerializer):
    event = EventSerializer()
    talks = TalkSerializer(many=True)

    class Meta:
        model = Program
        fields = ['event', 'day', 'talks'] 

