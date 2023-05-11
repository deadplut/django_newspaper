from django import template
from django.db.models import Count, F

from ..models import Categories

register = template.Library()


# @register.simple_tag()
# def get_categories():
#     return Categories.objects.all()


@register.inclusion_tag('feednews/cat_list.html')
def show_categories():
    # cats = Categories.objects.annotate(count_news=Count('catcat')).filter(catcat__is_published='1')
    cats = Categories.objects.annotate(count_news=Count('catcat'), filter=F('catcat__is_published'))

    return {'cats': cats}

    # return
