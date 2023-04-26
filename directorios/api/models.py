# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    correo = models.EmailField(null=True, blank=True)
    repeat = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username