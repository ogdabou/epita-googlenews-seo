from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^admin/add/rss$', 'news_site.views.addRss'),
    #url(r'^admin/request/request$', 'news_site.views.get_request', name='post_request'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^news/', include('news_site.urls')),
)
