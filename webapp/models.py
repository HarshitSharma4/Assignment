from django.db import models

class User(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=120)

    def __str__(self):
        return self.name
