from django.contrib.auth.models import User
from rest_framework import serializers
from nm.models import Game

from datetime import datetime

class GameSerializer(serializers.HyperlinkedModelSerializer):
    player_x = serializers.ReadOnlyField(source='player_x.username')
    player_y = serializers.ReadOnlyField(source='player_y.username')
    class Meta:
        model = Game
        fields = ['url', 'id', 'created', 'updated', 'cells', 'player_x', 'player_y']

class UserSerializer(serializers.ModelSerializer):
    games = serializers.HyperlinkedRelatedField(many=True, view_name='game-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'games']