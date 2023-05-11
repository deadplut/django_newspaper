from django import forms
from .models import Categories, News


# class NewsForm(forms.Form):
#     title = forms.CharField(max_length=200)
#     text = forms.CharField()
#     author = forms.CharField(max_length=200)
#     is_published = forms.BooleanField()
#     category = forms.ModelChoiceField(queryset=Categories.objects.all())
#     image = forms.ImageField()


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('title', 'text', 'author', 'is_published', 'category', 'image')
