from django.contrib import admin

from django.contrib import messages
from .forms import FeedForm
from .models import Article, Feed
from .FeedParser import FeedParser
from .NGram import NGram


def update_price(modeladmin, request, queryset):
    feedparser = FeedParser()
    ngram = NGram()

    for feed in queryset:
        articles = feedparser.parse(feed.url)

        for article in articles:
            article.save()
            ngram.computeNGrams(article.description_text, 2)
        modeladmin.message_user(request, ("Successfully crawled %d / %d feeds") % (len(queryset), len(articles)), messages.SUCCESS)

update_price.short_description = 'Crawl RSS feed'


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title_text', 'description_text', 'public_date')
    list_filter = ['public_date']
    search_fields = ['title_text']


class FeedAdmin(admin.ModelAdmin):
    list_display = ('url',)
    url = ['url']
    actions = [update_price]
    
admin.site.register(Article, ArticleAdmin)
admin.site.register(Feed, FeedAdmin)
