from django.db import models


class Bet(models.Model):
    match = models.ForeignKey('Match')
    winner = models.ForeignKey('Team')
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    ammount = models.DecimalField(max_digits=5, decimal_places=2)
