from django.contrib import admin

from django.contrib import messages
from .forms import FeedForm
from .models import Article, Feed
from .FeedParser import FeedParser
from .KeyWordsProcessor import KeyWordsProcessor
from .NGram import NGram
from goose import Goose


def update_price(modeladmin, request, queryset):
    feedparser = FeedParser()
    ngram = NGram()

    for feed in queryset:
        articles = feedparser.parse(feed.url)

        for x in range(0, len(articles), 1):
            article = articles[x]
            article.feed_id = feed.id
            g = Goose()
            g_article = g.extract(article.url)
            article.content_text = g_article.cleaned_text
            if g_article.top_image is not None:
                article.img_url = g_article.top_image.src
            article.save()
            ngram.computeNGrams(article.description_text, 2)
        modeladmin.message_user(request, ("Successfully crawled %d / %d feeds") % (len(queryset), len(articles)), messages.SUCCESS)

update_price.short_description = 'Crawl RSS feed'

def compute_keywords(modeladmin, request, feeds):
    keyWordsProcessor = KeyWordsProcessor()
    for feed in feeds:
        keyWordsProcessor.process(feed)

compute_keywords.short_description = 'Compute keywords on feed clusters'

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('feed_id', 'title_text', 'description_text', 'content_text', 'lemmatized_text', 'tf_idf_description_words', 'lemmatized_description',)
    list_filter = ['public_date']
    search_fields = ['title_text']


class FeedAdmin(admin.ModelAdmin):
    list_display = ('id', 'url',)
    url = ['url']
    actions = [update_price, compute_keywords]
    
admin.site.register(Article, ArticleAdmin)
admin.site.register(Feed, FeedAdmin)
