from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from nm.permissions import IsPlayerOrReadOnly

from nm.models import Game
from nm.serializers import GameSerializer, UserSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'games': reverse('game-list', request=request, format=format),
    })


class GameList(generics.ListCreateAPIView):
    """
    List all games, or create a new game.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def perform_create(self, serializer):
        serializer.save(player_x=self.request.user)


class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a game.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsPlayerOrReadOnly]

    queryset = Game.objects.all()
    serializer_class = GameSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer