from rest_framework import serializers
from nm.models import Game

from datetime import datetime

class GameSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    created = serializers.DateTimeField(default=datetime.now())
    updated = serializers.DateTimeField(required=False, allow_blank=True)
    cells = serializers.CharField(max_length=36)

    def create(self, validated_data):
        """
        Create and return a new `Game` instance, given the validated data.
        """
        return Game.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Game` instance, given the validated data.
        """
        instance.created = validated_data.get('created', instance.created)
        instance.updated = validated_data.get('updated', instance.updated)
        instance.cells = validated_data.get('cells', instance.cells)
        instance.save()
        return instance
