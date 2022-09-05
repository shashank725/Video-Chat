from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class RoomMember(models.Model):
    # name = models.ForeignKey(User, on_delete=models.CASCAD)
    name = models.CharField(max_length=200)
    uid = models.CharField(max_length=1000)
    room_name = models.CharField(max_length=200)
    insession = models.BooleanField(default=True)

    def __str__(self):
        return self.name