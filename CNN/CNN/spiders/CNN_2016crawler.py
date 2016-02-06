import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from CNN.items import CnnItem  # item class 
from scrapy.selector import Selector


class MySpider(CrawlSpider):
    name = "CNN"  # unique identifier for the spider
    allowed_domains = ['cnn.com']  # limits the crawl to this domain list
    start_urls = [
    'http://www.cnn.com/specials/politics/2016-election'
    ]  
    rules = [
        Rule(LinkExtractor(allow=r'/politics/'),
         callback='parse_item', follow=True)
    ]

    def parse_item(self, response):
        sel = Selector(response)
        results = []
        item = CnnItem()
        item['article_title'] = sel.xpath('.//h1[@class="pg-headline"]/text()').extract()
        item['article_author'] = sel.xpath('.//p[@class="metadata__byline"]/span/a/text()').extract()
        item['article_highlights'] = sel.xpath('.//div[@class="el__storyhighlights"]/ul/li/text()').extract()
        item['article_edsource'] = sel.xpath('//*[@id="body-text"]/div[1]/div[2]/p/cite/text()').extract()
        item['article_content'] = sel.xpath('//div[@class="zn-body__read-all"]/p[descendant-or-self::text()]').extract()
        item['article_timestamp'] = sel.xpath('.//p[@class="update-time"]/text()').extract()
        item['article_url'] = sel.xpath('/html/head/meta[9]/@content').extract()
        results.append(item)
        return results

