from django.db import models

# Create your models here.

class Widget(models.Model):
    item=models.CharField(max_length=80)

