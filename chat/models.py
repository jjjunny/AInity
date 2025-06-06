from django.db import models
from django.contrib.auth import get_user_model

class Room(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} @ {self.room}: {self.content}'
