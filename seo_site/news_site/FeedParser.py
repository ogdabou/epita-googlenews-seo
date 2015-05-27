import feedparser

from .models import Article

class FeedParser():

    def parse(self, url):
        rssFeed = feedparser.parse(url)

        articles = []
        for rssArticleRow in rssFeed.entries:
            article = Article()
            article.title_text = rssArticleRow['title']
            article.url = rssArticleRow['link']
            article.description_text = rssArticleRow['summary']
            articles.append(article)
            print article.url
        return articles