from django.contrib import admin
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    re_path('api/(?P<version>(v1|v2))/', include('api.user.urls'))
]
