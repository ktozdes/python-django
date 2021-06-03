from django.db import models

# Create your models here.
class MenuGroup(models.Model):
    name = models.CharField(max_length=200)
    rank = models.IntegerField(default=0, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True, null=True)
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)


class Menu(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    position = models.IntegerField(default=0, null=True)
    is_active = models.BooleanField(default=True)
    menu_group = models.ForeignKey(MenuGroup, on_delete=models.CASCADE, null=True)