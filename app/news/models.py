from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    rank = models.IntegerField(default=0, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)


class News(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    content = HTMLField(null=True)
    position = models.IntegerField(default=0, null=True)
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)



class Comments(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    position = models.IntegerField(default=0, null=True)
    is_active = models.BooleanField(default=True)
    news = models.ForeignKey(News, on_delete=models.CASCADE, null=True)