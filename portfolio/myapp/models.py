from django.db import models

# Create your models here.
class Portfolio(models.Model):
    name = models.CharField(max_length=200, null = True)
    skill = models.CharField(max_length = 300, null = True)
    email = models.CharField(max_length = 200, null = True)

    def __str__(self):
        return self.name
