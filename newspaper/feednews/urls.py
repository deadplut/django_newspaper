from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:cat_id>', views.render_category, name='category'),
    path('<int:post_id>', views.render_post, name='post'),

]