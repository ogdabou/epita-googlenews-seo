import feedparser

from .models import Article
from HTMLParser import HTMLParser

class FeedParser(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []

    def resetData(self):
        self.reset()
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return u' '.join(self.fed)

    def parse(self, url):
        rssFeed = feedparser.parse(url)

        articles = []
        for rssArticleRow in rssFeed.entries:
            article = Article()
            article.title_text = rssArticleRow['title']
            article.url = rssArticleRow['link']
            article.description_text = self.cleanhtml(rssArticleRow['summary'])
            articles.append(article)
            print article.url
        return articles

    def cleanhtml(self, html):
        self.resetData()
        self.feed(html)
        return self.get_data()
