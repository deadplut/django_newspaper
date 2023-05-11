from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .forms import NewsForm
from .models import News, Categories, Images


class NewsAbsract:
    model = News
    template_name = 'feednews/index.html'
    context_object_name = 'news'
    extra_context = {"title": "Newspaper",}
    # queryset = News.objects.select_related('image').filter(is_published='1')

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'Newspaper'
    #     return context


class ShowNews(NewsAbsract, ListView):
    def get_queryset(self):
        return News.objects.select_related('category').select_related('image').filter(is_published='1') #select_related для одного ко многим
        # МНОГИЕ КО МНОГИМ prefetch загуглить


class NewsCategory(NewsAbsract, ListView):
    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['cat_id'], is_published='1')


class ShowPost(NewsAbsract, DetailView):
    template_name = 'feednews/single_news.html'
    context_object_name = 'item'


class AddNews(CreateView):

    form_class = NewsForm
    template_name = "feednews/adding_news.html"
    success_url = reverse_lazy('post')

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'Newspaper'
    #     print('#'*33)
    #     print(self.form_class)
    #     return reverse_lazy('post')





#
# def render_adding_news(request):
#     if request.method == "POST":
#         form = NewsForm(request.POST, request.FILES)
#         if form.is_valid():
#             image = form.cleaned_data.pop('image')
#
#             img_obj = Images.objects.create(
#                                  title='test',
#                                  image=image
#                                  )
#             img_obj.save()
#
#             new_news = News.objects.create(
#                image=img_obj,
#                 **form.cleaned_data
#             )
#             new_news.save()
#
#             return HttpResponseRedirect(f"/{new_news.id}")
#     else:
#         form = NewsForm()
#     return render(request, "feednews/adding_news.html", {"form": form})


class PostUpdate(UpdateView):
    model = News
    fields = ['title']
    # success_url = 'post'


#переписать тэг на inclusion
# Написать собственный фильтр

