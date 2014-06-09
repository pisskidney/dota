from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=5096)
    logo_pattern = models.CharField(max_length=255,
                                    default="%s_team_logo_%dx%d")

    class Meta:
        app_label = 'ebets'
