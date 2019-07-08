from django.db import models

# Create your models here.
class BoardState(models.Model):
    a0 = models.CharField(max_length=1)
    a1 = models.CharField(max_length=1)
    a2 = models.CharField(max_length=1)
    a3 = models.CharField(max_length=1)
    a4 = models.CharField(max_length=1)
    a5 = models.CharField(max_length=1)
    b0 = models.CharField(max_length=1)
    b1 = models.CharField(max_length=1)
    b2 = models.CharField(max_length=1)
    b3 = models.CharField(max_length=1)
    b4 = models.CharField(max_length=1)
    b5 = models.CharField(max_length=1)
    c0 = models.CharField(max_length=1)
    c1 = models.CharField(max_length=1)
    c2 = models.CharField(max_length=1)
    c3 = models.CharField(max_length=1)
    c4 = models.CharField(max_length=1)
    c5 = models.CharField(max_length=1)
    d0 = models.CharField(max_length=1)
    d1 = models.CharField(max_length=1)
    d2 = models.CharField(max_length=1)
    d3 = models.CharField(max_length=1)
    d4 = models.CharField(max_length=1)
    d5 = models.CharField(max_length=1)
    e0 = models.CharField(max_length=1)
    e1 = models.CharField(max_length=1)
    e2 = models.CharField(max_length=1)
    e3 = models.CharField(max_length=1)
    e4 = models.CharField(max_length=1)
    e5 = models.CharField(max_length=1)
    f0 = models.CharField(max_length=1)
    f1 = models.CharField(max_length=1)
    f2 = models.CharField(max_length=1)
    f3 = models.CharField(max_length=1)
    f4 = models.CharField(max_length=1)
    f5 = models.CharField(max_length=1)
 
    class Meta:
        app_label = 'nightmouse_be'

    def __str__(self):
        return  "".join(vars(self).values())

class GameState(models.Model):
    winner = models.CharField(max_length=1)
    player_x = models.ForeignKey(User)
    player_y = models.ForeignKey(User)
    next_turn = models.ForeignKey(User)
    board_state = models.ForeignKey(BoardState)
    desc = models.CharField(max_length=20)

    def __str__(self):
        return player_x.username + " " + player_y.username
