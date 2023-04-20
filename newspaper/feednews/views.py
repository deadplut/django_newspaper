from django.http import HttpResponse
from django.shortcuts import render
from .models import News, Categories


def index(request):
    data = News.objects.select_related('image').all()[:3]
    data_cat = Categories.objects.all()
    context = {"news": data, "title": "Newspaper", "cats": data_cat}
    return render(request, "feednews/index.html", context=context)


def render_category(request, cat_id):
    data = News.objects.select_related('image').filter(category_id=cat_id)

    data_cat = Categories.objects.all()
    context = {"news": data, "title": "Newspaper", "cats": data_cat}
    return render(request, "feednews/index.html", context=context)


def render_post(request, post_id):
    data = News.objects.select_related('image').filter(id=post_id)
    data_cat = Categories.objects.all()

    context = {"news": data,
               "title": "Newspaper",
               "cats": data_cat}

    return render(request, "feednews/index.html", context=context)



# Здест напрашивается объединить эти функции