from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic.base import View


class SearchView(View):
    def get(self, request):
        return HttpResponse('Hello, World!', status=200)
