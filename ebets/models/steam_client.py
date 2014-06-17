from django.db import models
from django.conf import settings


class SteamClient(models.Model):
    player_info_pattern = models.CharField(
        max_length=1024,
        default='http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0\
002/?key={1}&steamids={2}'
    )

    def get_player_info_url(self, identifier):
        steam_api_key = settings['STEAM_API_KEY']
        url = self.player_info_pattern.replace('{1}', steam_api_key)
        url = url.replace('{2}', identifier)
        return url
