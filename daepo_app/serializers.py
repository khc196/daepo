from rest_framework import serializers
from .models import Thing, Request, Chat, Tackle

class ThingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thing
        fields = [
                'id',
                'name',
                'date',
                'points',
                'content',
                'reporting_date'
        ]
    def create(self, validated_data):
        return Thing.objects.create(**validated_data)

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = [
                'id',
                'name',
                'content',
                'reporting_date'
        ]
    def create(self, validated_data):
        return Request.objects.create(**validated_data)

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = [
                'id',
                'name',
                'content',
                'reporting_date'
        ]
    def create(self, validated_data):
        return Chat.objects.create(**validated_data)


class TackleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tackle
        fields = [
                'id',
                'thing_id',
                'content',
                'reporting_date'
        ]
    def create(self, validated_data):
        return Tackle.objects.create(**validated_data)
