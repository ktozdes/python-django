from django.contrib import admin

from .models import Category
from .models import News
from .models import Comment

admin.site.register(Category)
admin.site.register(News)
admin.site.register(Comment)
