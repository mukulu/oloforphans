from django.contrib import admin
from django import forms
from django.db.models import get_model
from apps.pages.models import Page, Category
from apps.pages.forms import ArticleAdminModelForm

class PageAdmin(admin.ModelAdmin):
	list_display=("heading","name","category","author","date_posted")
	form = ArticleAdminModelForm

class CategoryAdmin(admin.ModelAdmin):
	list_display=("name","description")

admin.site.register(Page,PageAdmin)
admin.site.register(Category,CategoryAdmin)
