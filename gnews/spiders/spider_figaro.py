from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector, Selector


class LeMondeSpider(CrawlSpider):
    name = 'figarospider'
    allowed_domains = ['lefigaro.fr']
    start_urls = [
        'http://www.lefigaro.fr/politique/2015/05/26/01002-20150526ARTFIG00180-l-ump-pourra-s-appeler-les-republicains.php']

    def parse(self, response):

        result =[]
        for node in response.xpath("//div[@class='fig-article-body']").extract():
            result.append(node)
            print node



