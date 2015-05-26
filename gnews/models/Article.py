__author__ = 'ogdabou'

from scrapy.item import Item, Field

# This class represents the model of an Article for the scrapy crawler
class Article(Item):
    title = Field()
    url = Field()
    summary = Field()
    content = Field()

