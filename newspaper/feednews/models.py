from django.db import models

# Create your models here.
from django.urls import reverse


class Images(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"  # множественное

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Тутул тянется из model.py")
    text = models.TextField()
    author = models.CharField(max_length=200)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField()
    image = models.ForeignKey("Images", on_delete=models.DO_NOTHING, blank=True, null=True, related_name='images_table')
    category = models.ForeignKey("Categories", on_delete=models.PROTECT, null=True, related_name='catcat')

    class Meta:
        ordering = ['-date_creation']
        verbose_name = "News"
        verbose_name_plural = "News"  # множественное

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post", kwargs={"pk": self.pk})


class Categories(models.Model):
    name = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse("category", kwargs={"cat_id": self.pk})

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"  # множественное

    def __str__(self):
        return self.name


class Books(models.Model):
    name = models.CharField(max_length=200, default='')
    price = models.IntegerField()
    pages = models.IntegerField()
    author = models.CharField(max_length=255, default='')
    year = models.CharField(max_length=255, default='')
    comment = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"  # множественное
# TODO Как использовать OR XOR class q
