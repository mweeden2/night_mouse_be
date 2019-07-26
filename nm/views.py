from rest_framework import generics

from nm.models import Game
from nm.serializers import GameSerializer


class GameList(generics.ListCreateAPIView):
    """
    List all games, or create a new game.
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a game.
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer