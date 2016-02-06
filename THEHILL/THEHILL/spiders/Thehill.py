import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from THEHILL.items import ThehillItem  # item class 
from scrapy.selector import Selector



class MySpider(CrawlSpider):
    name = "thehill"  # unique identifier for the spider
    allowed_domains = ['thehill.com']  # limits the crawl to this domain list
    start_urls = [
    'http://thehill.com/blogs/ballot-box'
    ]
    rules = [
        Rule(LinkExtractor(allow=r'/ballot-box/'),
         callback='parse_item', follow=True)
    ]

    def parse_item(self, response):
        sel = Selector(response)
        results = []
        item = ThehillItem()
        item['article_title'] = sel.xpath('//h1[@class="title"]/text()').extract()
        #item['article_imagecaption'] = sel.xpath('.//div[@class="entry-content"]/div[3]/figure[1]/figcaption[1]/span[1]/text()').extract()
        item['article_author'] = sel.xpath('//*[@id="content"]/article/div[1]/p/span/text()').extract()
        #item['article_highlights'] = sel.xpath('.//div[@class="el__storyhighlights"]/ul/li/text()').extract()
        #item['article_edsource'] = sel.xpath('//*[@id="body-text"]/div[1]/div[2]/p/cite/text()').extract()
        item['article_content'] = sel.xpath('//div[@class="field-item even"]/div[descendant-or-self::text()]').extract()
        item['article_timestamp'] = sel.xpath('//*[@id="content"]/span/text()').extract()
        item['article_url'] = sel.xpath('/html/head/meta[15]/@content').extract()
        results.append(item)
        return results
