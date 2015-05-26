from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector, Selector


class LeMondeSpider(CrawlSpider):
    name = '20minutesspider'
    allowed_domains = ['20minutes.fr']
    start_urls = [
        'http://www.20minutes.fr/high-tech/1616287-20150526-helios-premier-casque-energie-solaire']

    def parse(self, response):
        for node in response.xpath("//div[@role='main']/p/text() | //a[not(@class)]/em/text() | //p/a[not(@xtclib)]/text() | //p[not(@class)]/span/text()").extract():
            print node



