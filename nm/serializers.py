from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.reverse import reverse

from datetime import datetime

from nm.models import Game

class GameSerializer(serializers.HyperlinkedModelSerializer):
    player_x = serializers.ReadOnlyField(source='player_x.username')
    player_y = serializers.ReadOnlyField(source='player_y.username')
    class Meta:
        model = Game
        fields = ['url', 'id', 'created', 'updated', 'cells', 'player_x', 'player_y']

class UserSerializer(serializers.ModelSerializer):
    games = serializers.SerializerMethodField('get_all_games')

    # special sauce partially from https://stackoverflow.com/questions/35546825/django-rest-framework-custom-hyperlink-field-in-serializer 
    def get_all_games(self, obj):
        return [reverse('game-detail', args=[x.id], request=self.context['request']) for x in list(obj.games_x.all() | obj.games_y.all())]

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'games']