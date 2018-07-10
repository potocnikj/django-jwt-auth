from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
