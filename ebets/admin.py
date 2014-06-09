from django.contrib import admin
from ebets.models import Player, Match, Team, Event


class PlayerAdmin(admin.ModelAdmin):
    fields = ('nickname', 'team', 'first_name', 'last_name',
              'pic_pattern', 'description')
    list_display = ('nickname', 'team')


admin.site.register(Player, PlayerAdmin)


class TeamAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'logo_pattern')
    list_display = ('name',)


admin.site.register(Team, TeamAdmin)


class MatchAdmin(admin.ModelAdmin):
    fields = ('radiant', 'dire', 'date', 'event', 'description', 'winner',
              'over')
    list_display = ('radiant', 'dire', 'date', 'event')


admin.site.register(Match, MatchAdmin)


class EventAdmin(admin.ModelAdmin):
    fields = ('name', 'logo', 'description', 'online', 'offline')
    list_display = ('name',)


admin.site.register(Event, EventAdmin)
