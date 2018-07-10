from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^users/$', views.users),
    url(r'^users/(?P<id>[0-9]+)/$', views.user),
]