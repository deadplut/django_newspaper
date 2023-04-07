from django.http import HttpResponse
from django.shortcuts import render
from .models import News, Images


def index(request):
    data = News.objects.order_by('-date_creation').select_related('image_id').all()[:3]



    return render(request, "feednews/index.html", {"news": data})