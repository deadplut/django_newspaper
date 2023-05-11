from django.contrib import admin

from .models import *


# class ImagesAdmin(admin.TabularInline):
#     model = Images
# TODO дз: Как сделать красиво InlineModelAdmin
# TODo посмотреть аттрибуты
# TODo сделать категории в include
# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    # задаем поля для админки
    list_display = ("title", "is_published", "date_creation", "date_update")
    search_fields = ["title", "date_creation", "is_published"]
    list_editable = ("is_published",)
    list_filter = ("date_creation", "is_published")
    readonly_fields = ("date_update", "date_creation")
    # inlines = (ImagesAdmin,)


class NewsInline(admin.TabularInline):
    model = News


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    inlines = (NewsInline,)


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_filter = ("year", "price")


# admin.site.register(Categories)
admin.site.register(Images)
