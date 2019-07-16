from rest_framework import serializers
from nm.models import Game

class GameSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    created = serializers.DateTimeField()
    updated = serializers.DateTimeField()
    cells = models.CharField(max_length=36)
