from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector, Selector


class LeMondeSpider(CrawlSpider):
    name = 'parisienspider'
    allowed_domains = ['parisien.fr']
    start_urls = [
        'http://www.leparisien.fr/politique/les-republicains-sarkozy-accuse-hollande-d-avoir-porte-l-affaire-au-tribunal-26-05-2015-4804815.php']

    def parse(self, response):

        result =[]
        for node in response.xpath("//h2/text() | //h2/a/text() | //div[not(@class='vertical-middle text-center')]/p[not(@class)]/text() | //p[not(@class)]/a/text() | //div[not(@class='contTitre m5t')]/p[not(@class)]/text() ").extract():
            result.append(node)
            print node



