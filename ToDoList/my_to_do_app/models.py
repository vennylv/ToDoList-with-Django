from django.db import models

# Create your models here.
class TOdo(models.Model):
    content = models.CharField(max_length=255)
    