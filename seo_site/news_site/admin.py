from django.contrib import admin

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title_text', 'description_text', 'public_date')
    list_filter = ['public_date']
    search_fields = ['title_text']
    
admin.site.register(Article, ArticleAdmin);