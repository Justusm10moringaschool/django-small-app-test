from django.db import models

# Create your models here.

class List(models.Model):
    title = models.CharField(max_length=200)

    created = models.DateTimeField(auto_now_add=True)

    trip = models.CharField(max_length=10)

    def __str__(self):
        return self.title
    