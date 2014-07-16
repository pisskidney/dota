import urllib2
import json

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic.base import View
from django.contrib.auth import get_user_model, login, authenticate, logout

from .search import SearchView


User = get_user_model()


class LoginView(View):
    def get(self, request):
        #Full profile url.
        #Eg: http://steamcommunity.com/openid/id/76561198076687907
        steam_url = request.GET.get('openid.claimed_id', None)

        if steam_url is None:
            return redirect('search')

        #17 digit steam id
        steam_id = steam_url.split('/')[-1]

        #The url we'll call for the profile info
        #We could use getattr here but we want it to fail loudly.
        steam_profile_url_pattern = settings.STEAM_API_KEY_PATTERN
        steam_profile_url = steam_profile_url_pattern.replace('{1}', steam_id)

        #Get the profile info
        response = urllib2.urlopen(steam_profile_url)
        info = json.loads(response.read())['response']['players'][0]

        user, _ = User.objects.get_or_create(identifier=steam_id)
        user.update_from_steam_data(info)

        user = authenticate(identifier=user.identifier)
        login(request, user)

        return redirect('home')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')

