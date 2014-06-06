from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=5096)
    logo = models.CharField(max_length=1024)

    class Meta:
        app_label = 'ebets'
