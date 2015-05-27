from django.contrib import admin

from django.contrib import messages

from .models import Article, Feed

def coucouHiboux():
    print "coucouHiboux"

def update_price(modeladmin, request, queryset):
    print "lol"
    modeladmin.message_user(request, ("Successfully updated price for %d rows") % (45,), messages.SUCCESS)
update_price.short_description = 'Update price of selected rows'

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
