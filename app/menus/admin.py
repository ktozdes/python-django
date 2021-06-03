from django.contrib import admin

# Register your models here.

from .models import MenuGroup, Menu

admin.site.register(MenuGroup)
admin.site.register(Menu)
