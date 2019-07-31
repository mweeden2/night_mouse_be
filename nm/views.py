from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import permissions

from django.contrib.auth.models import User

from nm.permissions import IsPlayerOrReadOnly
from nm.models import Game
from nm.serializers import GameSerializer, UserSerializer



class GameViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically providers `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsPlayerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(player_x=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically providers `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer