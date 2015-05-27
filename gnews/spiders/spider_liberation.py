from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector, Selector


class LeMondeSpider(CrawlSpider):
    name = 'liberationspider'
    allowed_domains = ['liberation.fr']
    start_urls = [
        'http://www.liberation.fr/monde/2015/05/26/iran-ouverture-du-proces-du-correspondant-du-washington-post-accuse-d-espionnage_1316566']

    def parse(self, response):

        result =[]
        for node in response.xpath("//div[not(@class)]/p/text() ").extract():
            result.append(node)
            print node



