from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=5096)
    pic = models.CharField(max_length=1024)
