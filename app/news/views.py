from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator

from django_seed import Seed
from django.utils.crypto import get_random_string

from .models import Category
from .models import News

import random

def index(request):
    context ={}
    context["main_categories"] = Category.objects.filter(parent_id__isnull=True)

    news = News.objects.filter(status='published').order_by('-created_at')
    paginator = Paginator(news, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context["list"] = page_obj

    return render(request, 'index.html', context)

def show(request, slug):
    current_news = News.objects.filter(slug__iexact = slug)
    if current_news.exists():
        current_news = current_news.first()
    else:
        return HttpResponse('<h1>Post Not Found</h1>')
    context = {
        'current_news': current_news
    }
    return render(request, 'show.html', context)

def categories(request):

    seeder = Seed.seeder()
    seeder.add_entity(News, 10, {
        'category': Category.objects.order_by('?')[0],
        'slug': get_random_string(20),
    })
    inserted_pks = seeder.execute()
    return HttpResponse("news categories." )

def category(request, slug):
    return HttpResponse("news categories slug: %s." % slug)
