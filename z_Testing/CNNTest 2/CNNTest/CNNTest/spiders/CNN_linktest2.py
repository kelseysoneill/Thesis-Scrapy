import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from CNNTest.items import MyItem  # item class 
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from html2text import HTML2Text
        

class MySpider(CrawlSpider):
    name = "CNNcrawl2"  # unique identifier for the spider
    allowed_domains = ['cnn.com/specials/politics/']  # limits the crawl to this domain list
    start_urls = [
    'http://www.cnn.com/specials/politics/2016-election'
    ]  # first url to crawl in domain

    rules = [
        Rule(LinkExtractor(), follow=True),
        Rule(LinkExtractor(), callback='parse_item')
        ]

    def parse_item(self, response):
        sel = Selector(response)
        results = []
        item = MyItem()
        item['article_title'] = sel.xpath('.//h1[@class="pg-headline"]/text()').extract()
        item['article_author1'] = sel.xpath('.//p[@class="metadata__byline"]/span/text()').extract()
        item['article_author2'] = sel.xpath('.//p[@class="metadata__byline"]/span/a/text()').extract()
        item['article_highlights'] = sel.xpath('.//div[@class="el__storyhighlights"]/ul/li/text()').extract()
        
        item['article_edsource'] = sel.xpath('//*[@id="body-text"]/div[1]/div[2]/p/cite/text()').extract()

        item['article_content'] = sel.xpath('//div[@class="pg-rail-tall__body"]//p/text()').extract()

        item['article_timestamp'] = sel.xpath('.//p[@class="update-time"]/text()').extract()


        results.append(item)
        return results
