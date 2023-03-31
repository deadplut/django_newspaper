from django.http import HttpResponse
from django.shortcuts import render
from .models import News


def index(request):
    data = News.objects.all()
    return render(request, "feednews/index.html", {"news": data})