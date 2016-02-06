import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from CNNTest.items import MyItem  # item class 
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
import html2text

class MySpider(CrawlSpider):
    name = "CNN_content"  # unique identifier for the spider
    allowed_domains = ['cnn.com']  # limits the crawl to this domain list
    start_urls = [
    'http://www.cnn.com/2016/02/01/politics/iowa-caucus-polling/index.html'
    ]  # first url to crawl in domain

    def parse(self, response):
        sel = Selector(response)
        results = []
        item = MyItem()
        item['article_title'] = sel.xpath('.//h1[@class="pg-headline"]/text()').extract()
        item['article_author1'] = sel.xpath('.//p[@class="metadata__byline"]/span/text()').extract()
        item['article_author2'] = sel.xpath('.//p[@class="metadata__byline"]/span/a/text()').extract()
        item['article_highlights'] = sel.xpath('.//div[@class="el__storyhighlights"]/ul/li/text()').extract()
        
        item['article_edsource'] = sel.xpath('//*[@id="body-text"]/div[1]/div[2]/p/cite/text()').extract()

        item['article_content'] = sel.xpath('.//div[@class="zn-body__read-all"]/p/text()').extract()
        item['article_timestamp'] = sel.xpath('.//p[@class="update-time"]/text()').extract()
        
        
        converter = html2text.HTML2Text()
        converter.ignore_links = True
        return converter.handle(item['article_content'])
        
        results.append(item)
        return results