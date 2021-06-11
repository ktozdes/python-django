from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    rank = models.IntegerField(default=0, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    class Meta:
        verbose_name_plural = 'Categories'
        indexes = [
            models.Index(fields=['name'], name='category__name'),
        ]

class News(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    content = HTMLField(null=True)
    position = models.IntegerField(default=0, null=True)
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    class Meta:
        verbose_name_plural = 'News'
        indexes = [
            models.Index(fields=['name'], name='news__name'),
            models.Index(fields=['name', '-created_at'], name='news__name__created_at_desc'),
            models.Index(fields=['name', '-updated_at'], name='news__name__updated_at_desc')
        ]

class Comment(models.Model):
    comment =  models.TextField()
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)