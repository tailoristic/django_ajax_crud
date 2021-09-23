from django.db import models

class UserModel(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=150)
    password = models.CharField(max_length=100)