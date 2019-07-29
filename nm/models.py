from django.db import models


class Game(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True, blank=True)
    cells = models.CharField(max_length=36)
    player_x = models.ForeignKey('auth.User', related_name='player_x', on_delete=models.CASCADE)
    player_y = models.ForeignKey('auth.User', related_name='player_y', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['created']
