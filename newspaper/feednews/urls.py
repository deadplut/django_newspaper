from django.urls import path

from . import views

urlpatterns = [
    path('', views.ShowNews.as_view(), name='index'), #нюанс
    path('category/<int:cat_id>', views.NewsCategory.as_view(), name='category'),
    path('<int:pk>', views.ShowPost.as_view(), name='post'),
    path('add_news/', views.AddNews.as_view(), name='adding_news'),
    path('<int:pk>/edit/', views.PostUpdate.as_view(), name='update_news'),



]