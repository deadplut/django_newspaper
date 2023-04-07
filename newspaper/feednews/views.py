from django.http import HttpResponse
from django.shortcuts import render
from .models import News, Categories


def index(request):
    data = News.objects.select_related('image').all()[:3]
    data_cat = Categories.objects.all()
    context = {"news": data, "title": "Newspaper", "cats": data_cat}
    return render(request, "feednews/index.html", context=context)


"""
1) вывести категории, должны быть кликабельными и чтобы 
подсказка url создать  


"""