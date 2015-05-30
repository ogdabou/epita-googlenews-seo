from django.contrib import admin
#from django.utils.html import format_html_join
#from django.utils.safestring import mark_safe
from django.contrib import messages
#from .forms import FeedForm
from .models import Article, Feed
from django.http import HttpResponse
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
        modeladmin.message_user(request, ("Successfully crawled %d / %d feeds") % (len(queryset), len(articles)), messages.SUCCESS)

update_price.short_description = 'Crawl RSS feed'

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
    list_filter = ['public_date']
    search_fields = ['title_text']
    #readony_field = ('feed_keywords')
    
    #def feed_keywords(self,Feed):
     #   return format_html_join(
      #      mark_safe('<br/>'),
       #     '{}',
        #    ((line,) for line in Feed.objects.all()[:5]),
        #)or "<span class='errors'>I can't determine this address.</span>" 
         # short_description functions like a model field's verbose_name
    #feed_keywords.short_description = "keywords"
         # in this example, we have used HTML tags in the output
    #feed_keywords.allow_tags = True
    
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
    actions = [update_price, compute_keywords, export_csv]
    
    
admin.site.register(Article, ArticleAdmin)
admin.site.register(Feed, FeedAdmin)
