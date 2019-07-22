from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from nm.models import Game
from nm.serializers import GameSerializer

@csrf_exempt
def game_list(req):
    """
    List all games, or create a new game.
    """
    if req.method == 'GET':
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif req.method == 'POST':
        data = JSONParser().parse(req)
        serializer = GameSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def game_detail(req, pk):
    """
    Retrieve, update or delete a game.
    """
    try:
        game = Game.objects.get(pk=pk)
    except Game.DoesNotExist:
        return HttpResponse(status=404)

    if req.method == 'GET':
        serializer = GameSerializer(game)
        return JsonResponse(serializer.data)

    elif req.method == 'PUT':
        data = JSONParser().parse(req)
        serializer = GameSerializer(game, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif req.method == 'DELETE':
        game.delete()
        return HttpResponse(status=204)