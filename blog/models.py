from django.db import models
from datetime import datetime
from django.utils.translation import gettext as _

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='blog/images/')
    data = models.DateField()

    def __str__(self):
        return self.title
