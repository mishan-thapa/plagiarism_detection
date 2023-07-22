from django.db import models

# Create your models here.
class words(models.Model):
    sentence = models.CharField(max_length=100)

def __str__(self):
    return f"{self.sentence}" 