from django.contrib import admin
#from django.utils.html import format_html_join
#from django.utils.safestring import mark_safe
from django.contrib import messages
#from .forms import FeedForm
from .models import Article, Feed
from django.http import HttpResponse
from .forms import FeedForm
from .models import Article, Feed, Request
from .FeedParser import FeedParser
from .KeyWordsProcessor import KeyWordsProcessor
from .Cooccurrence import Cooccurrence
from .NGram import NGram
from goose import Goose


def crawl_feeds(modeladmin, request, queryset):
    feedparser = FeedParser()
    ngram = NGram()

    for feed in queryset:
        articles = feedparser.parse(feed.url)

        for x in range(0, len(articles), 1):
            article = articles[x]
            article.feed_id = feed.id
            g = Goose()
            g_article = g.extract(article.url)
            if g_article.cleaned_text != "" and g_article.cleaned_text is not None:
                article.content_text = g_article.cleaned_text
                if g_article.top_image is not None:
                    article.img_url = g_article.top_image.src
                article.save()
        modeladmin.message_user(request, ("Successfully crawled %d feeds and %d articles") % (len(queryset), len(articles)), messages.SUCCESS)

crawl_feeds.short_description = 'Crawl RSS feed'

def compute_keywords(modeladmin, request, feeds):
    keyWordsProcessor = KeyWordsProcessor()
    for feed in feeds:
        feed.keywords = keyWordsProcessor.process(feed)
        feed.save()

compute_keywords.short_description = 'Compute keywords on feed clusters'



class ArticleAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title_text', 'description_text', 
                'content_text', 'public_date','feed_id')})),
    list_display = ('feed_id', 'title_text', 'description_text',
                     'content_text', 'lemmatized_text', 'tf_idf_description_words', 
                     'lemmatized_description',)

def compute_text(modeladmin, request, feeds):
    keyWordsProcessor = KeyWordsProcessor()
    keyWordsProcessor.process_content()


compute_text.short_description = 'Compute content on database'

def compute_request(modeladmin, request, request_object):
    coocc = Cooccurrence()
    coocc.process(request_object)

compute_request.short_description = 'Compute request'

    
def export_csv(modeladmin, request, queryset):
        import csv
        from django.utils.encoding import smart_str
        response = HttpResponse()
        response['Content-Disposition'] = 'attachment; filename=mymodel.csv'
        writer = csv.writer(response, csv.excel)
        response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
        writer.writerow([
            smart_str("Keywords"),
        ])
        for obj in queryset:
            writer.writerow([
                smart_str(obj.keywords),
            ])
        return response
export_csv.short_description = u"Export CSV"     
        
class FeedAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'keywords')
    url = ['url']
    actions = [crawl_feeds, compute_keywords, compute_text,export_csv]

class RequestAdmin(admin.ModelAdmin):
    list_display = ('request', 'corrected_request', 'results')
    request = ['request']
    actions = [compute_request]
    
admin.site.register(Article, ArticleAdmin)
admin.site.register(Feed, FeedAdmin)
admin.site.register(Request, RequestAdmin)