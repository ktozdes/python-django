from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='news.index'),
    path('categories', views.categories, name='news.category'),
    path('category/<slug:slug>', views.category, name='news.category.index'),
    path('<slug:slug>', views.show, name='news.show'),
]