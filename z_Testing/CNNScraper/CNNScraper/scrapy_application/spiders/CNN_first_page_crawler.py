import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_application.items import MyItem  # item class 
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector

class MySpider(CrawlSpider):
    name = "CNN"  # unique identifier for the spider
    allowed_domains = ['cnn.com']  # limits the crawl to this domain list
    start_urls = ['http://www.cnn.com/2015/10/09/politics/john-kasich-super-pac-marco-rubio/index.html']  # first url to crawl in domain

    def parse(self, response):
        sel = Selector(response)
        articles = sel.xpath('//article')
        results = []

        for articles in articles:
            item = MyItem()
            item['article_title'] = articles.xpath('.//html/body/div[4]/article/div[1]/h1/text()').extract()
            results.append(item)
        return results