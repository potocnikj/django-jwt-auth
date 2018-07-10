from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^users/$', views.users, name='users'),
    url(r'^users/authenticate/$', views.authenticate, name='authenticate'),
    url(r'^users/authorize/$', views.authorize, name='authorize'),
    url(r'^users/(?P<id>[0-9]+)/$', views.user, name='user'),
]
