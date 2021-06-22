from django.contrib import admin
from django.forms import ModelForm

from .models import Category
from .models import News
from .models import Comment

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("name",)}
	list_display = ('name', 'rank', 'is_active', 'get_news_count')
	list_filter = ('created_at',)
	search_fields = ('name',)
	ordering = ['name']
	actions = ['disactivate', 'activate']

	fields = ('name', 'slug', 'parent', ('rank', 'is_active'))

	def get_news_count(self, obj):
	    return obj.news_set.count()

	@admin.action(description='Disactivate categories')
	def disactivate(modeladmin, request, queryset):
	    count = queryset.update(is_active=False)
	    if count > 0:
	    	modeladmin.message_user(request, 'Selected categories are disactivated')

	@admin.action(description='Activate categories')
	def activate(modeladmin, request, queryset):
	    count = queryset.update(is_active=True)
	    if count > 0:
	    	modeladmin.message_user(request, 'Selected categories are activated')

class NewsAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("name",)}
	list_display = ('name', 'is_active', 'is_featured', 'get_category')
	list_filter = ('created_at',)
	search_fields = ('name',)
	actions = ['disactivate', 'activate']

	def get_category(self, obj):
		return obj.category.name
	get_category.short_description = 'Category'

	@admin.action(description='Disactivate news')
	def disactivate(modeladmin, request, queryset):
	    count = queryset.update(is_active=False)
	    if count > 0:
	    	modeladmin.message_user(request, 'Selected news are disactivated')

	@admin.action(description='Activate news')
	def activate(modeladmin, request, queryset):
	    count = queryset.update(is_active=True)
	    if count > 0:
	    	modeladmin.message_user(request, 'Selected news are activated')


admin.site.register(Category, CategoryAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Comment)


