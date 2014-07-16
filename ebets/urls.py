from ebets import views
from django.conf.urls import patterns, url
from django.views.decorators.csrf import csrf_exempt


urlpatterns = patterns('',
    url(r'^$', views.SearchView.as_view(), name='home'),
    url(r'^login/', views.LoginView.as_view(), name='login'),
    url(r'^logout/', views.LogoutView.as_view(), name='logout'),
)
