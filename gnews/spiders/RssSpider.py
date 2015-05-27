__author__ = 'ogdabou'

from scrapy.spider import Spider
from gnews.models.Article import Article
from gnews.models.Feed import Feed
import feedparser

class RssSpider(Spider):
    name = "gnews-rss"
    allowed_domains = ['news.google.com']
    start_urls = [
        'https://news.google.com/news?cf=all&ned=us&hl=en&topic=h&ncl=dCctbNMCJQe_TGMFJSdUQBcA-2K9M&cf=all&output=rss']

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
        yield feed
