__author__ = 'ogdabou'

from scrapy.spider import Spider
import feedparser

class RssSpider(Spider):
    name = "gnews-rss"
    allowed_domains = ['news.google.com']
    start_urls = [
        'https://news.google.com/news?pz=1&cf=all&ned=fr&hl=fr&topic=t&ncl=dw795LYCcKHgS9MAhRGZSfvMEVTWM&output=rss']

    def parse(self, response):
        ## feedParser returns an entry list with all the details
        rssFeed = feedparser.parse(self.start_urls[0])

        for rssArticleRow in rssFeed.entries:
            print rssArticleRow
            lol = Article()

        print("Parsing feed %s", self.start_urls[0])
        print(rssFeed)
