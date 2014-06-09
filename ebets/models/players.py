from django.db import models


class Player(models.Model):
    nickname = models.CharField(max_length=255)
    team = models.ForeignKey('Team', related_name='players')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    pic_pattern = models.CharField(max_length=255,
                                   default='%s_player_pic_%dx%d')
    description = models.CharField(max_length=5096)

    class Meta:
        app_label = 'ebets'
