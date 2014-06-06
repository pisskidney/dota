from django.db import models


class Match(models.Model):
    radiant = models.ForeignKey('Team', related_name='radiant_matches')
    dire = models.ForeignKey('Team', related_name='dire_matches')
    date = models.DateTimeField(default=False)
    event = models.ForeignKey('Event')
    description = models.CharField(max_length=5096)
    winner = models.ForeignKey('Team', related_name='won_matches',
                               default=None)
    over = models.BooleanField(default=False)

    class Meta:
        app_label = 'ebets'


class Event(models.Model):
    name = models.CharField(max_length=1024)
    logo = models.CharField(max_length=1024)
    description = models.CharField(max_length=5096)
    online = models.BooleanField(default=True)
    offline = models.BooleanField(default=False)

    class Meta:
        app_label = 'ebets'
