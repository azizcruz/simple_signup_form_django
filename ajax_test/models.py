from django.db import models

# Create your models here.

class TinyForm(models.Model):
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self):
        return self.username
