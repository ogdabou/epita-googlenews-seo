from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector


class LeMondeSpider(CrawlSpider):
    name = "lemonde"
    allowed_domains = ['lemonde.fr']
    start_urls = [
        'http://www.lemonde.fr/football/article/2015/05/25/le-real-madrid-limoge-son-entraineur-carlo-ancelotti_4640261_1616938.html']

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.select("//h1[@itemprop='Headline']/text()")
        print titles
