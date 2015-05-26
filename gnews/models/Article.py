__author__ = 'ogdabou'

from scrapy.item import Item, Field

class Article(Item):
    name = "gnews"
    url = Field()
    link = Field()
    summary = Field()
    content = Field()

