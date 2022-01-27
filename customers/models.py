from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    number = models.CharField(max_length=15)
    location = models.CharField(max_length=50)
    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name