from django.urls import path
from .views import GetUsers


urlpatterns = [
    path('users/', GetUsers.as_view(), name="users-all")
]