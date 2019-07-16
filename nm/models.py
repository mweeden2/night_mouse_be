from django.db import models


class Game(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField()
    cells = models.CharField(max_length=36)

    class Meta:
        ordering = ['created']
