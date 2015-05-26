__author__ = 'ogdabou'

from .Article import Article
from scrapy.item import Item, Field

# This class represents a Feed model used in the scrapy crawler
class Feed(Article):
    articles = Field()

