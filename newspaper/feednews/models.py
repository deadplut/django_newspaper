from django.db import models


# Create your models here.

class Images(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.CharField(max_length=200)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField()
    image_id = models.ForeignKey(Images, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title