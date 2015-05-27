from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector, Selector


class LeMondeSpider(CrawlSpider):
    name = 'lemondespider'
    allowed_domains = ['lemonde.fr']
    start_urls = [
        'http://www.lemonde.fr/football/article/2015/05/25/le-real-madrid-limoge-son-entraineur-carlo-ancelotti_4640261_1616938.html']

    def parse(self, response):

        result =[]
        for node in response.xpath("//p[not(@class)]/text() | //p/em/text()").extract():
            #result.append(node)
            print node



