from django.contrib import admin
from ebets.models import Player, Match, Team, Event


class PlayerAdmin(admin.ModelAdmin):
    fields = ('nickname', 'team', 'first_name', 'last_name',
              'pic', 'pic_pattern', 'description')


admin.site.register(Player, PlayerAdmin)


class TeamAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'logo', 'logo_pattern')


admin.site.register(Team, TeamAdmin)


class MatchAdmin(admin.ModelAdmin):
    fields = ('radiant', 'dire', 'date', 'event', 'description', 'winner',
              'over')


admin.site.register(Match, MatchAdmin)


class EventAdmin(admin.ModelAdmin):
    fields = ('name', 'logo', 'description', 'online', 'offline')


admin.site.register(Event, EventAdmin)
