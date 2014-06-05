from cranky import views
from django.conf.urls import patterns, url
from django.views.decorators.csrf import csrf_exempt


urlpatterns = patterns('',
    url(r'^$', views.SearchView.as_view(), name='search'),
)
