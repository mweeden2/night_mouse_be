from rest_framework import serializers
from nm.models import Game

from datetime import datetime

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'create', 'updated', 'cells']