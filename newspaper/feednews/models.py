from django.db import models


# Create your models here.

class Images(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"  # множественное

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.CharField(max_length=200)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField()
    image = models.ForeignKey("Images", on_delete=models.DO_NOTHING, blank=True, null=True)
    category = models.ForeignKey("Categories", on_delete=models.PROTECT, null=True)

    class Meta:
        ordering = ['-date_creation']
        verbose_name = "News"
        verbose_name_plural = "News" # множественное

    def __str__(self):
        return self.title


class Categories(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"  # множественное

    def __str__(self):
        return self.name


