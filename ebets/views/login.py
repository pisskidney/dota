from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic.base import View
from .search import SearchView


class LoginView(View):
    def get(self, request):

        #Full profile url.
        #Eg: http://steamcommunity.com/openid/id/76561198076687907
        steam_url = request.GET.get('openid.claimed_id', None)
        
        if steam_url is None:
            return redirect('search')

        #17 digit steam id
        steam_id = steam_url.split('/')[-1]

        urllib2.



        


        return redirect('search')
