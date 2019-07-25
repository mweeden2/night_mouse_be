from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from nm.models import Game
from nm.serializers import GameSerializer


@api_view(['GET', 'POST'])
def game_list(req, format=None):
    """
    List all games, or create a new game.
    """
    if req.method == 'GET':
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)

    elif req.method == 'POST':
        serializer = GameSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def game_detail(req, pk, format=None):
    """
    Retrieve, update, or delete a game.
    """
    try:
        game = Game.objects.get(pk=pk)
    except Game.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if req.method == 'GET':
        serializer = GameSerializer(game)
        return Response(serializer.data)

    elif req.method == 'PUT':
        serializer = GameSerializer(game, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif req.method == 'DELETE':
        game.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)