from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

class CustomUser(AbstractUser):
    pass
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    admin = models.BooleanField(default=False)
    website = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + self.last_name
    
    def isAdmin(self):
        return self.admin

    def get_absolute_url(self):
        return reverse('overseer', kwargs={'pk': self.pk})
