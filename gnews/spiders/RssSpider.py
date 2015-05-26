__author__ = 'ogdabou'

from scrapy.spider import Spider
from gnews.models.Article import Article
from gnews.models.Feed import Feed
import feedparser

class RssSpider(Spider):
    name = "gnews-rss"
    allowed_domains = ['news.google.com']
    start_urls = [
        'https://news.google.com/news?pz=1&cf=all&ned=fr&hl=fr&topic=t&ncl=dw795LYCcKHgS9MAhRGZSfvMEVTWM&output=rss']

    def parse(self, response):
        # feedParser returns an entry list with all the details
        rssFeed = feedparser.parse(self.start_urls[0])
        feed = Feed()
        feed['articles'] = []
        for rssArticleRow in rssFeed.entries:
            article = Article()
            article['title'] = rssArticleRow['title']
            article['url'] = rssArticleRow['link']
            article['summary'] = rssArticleRow['summary']
            feed['articles'].append(dict(article))
            print feed
        yield feed
