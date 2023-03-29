from django.db import models


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=32)
    text = models.TextField()
    author = models.CharField(max_length=32)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField()