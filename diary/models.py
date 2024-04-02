from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User
from user.models import UserModel
from uuid import uuid4

class Moods(models.IntegerChoices):
    happy = 1, '🙂'
    neutral = 2, '😶'
    sad = 3, '🙁'

class DiaryEntry(models.Model):
    uuid = models.CharField(max_length=36, default=uuid4, null=False)
    title = models.CharField(max_length=50, null=False)
    date_time = models.DateTimeField(default=timezone.now, null=False)
    location = models.CharField(max_length=200, default='', null=False, blank=True)
    # mood = models.CharField(max_length=100, default='', null=False)
    mood = models.IntegerField(choices=Moods.choices, default=2, null=False)
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    content = models.CharField(max_length=8000, default='', null=False, blank=True)
    def __str__(self):
        return self.title
