import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from HUFFPO.items import HuffpoItem  # item class 
from scrapy.selector import Selector



class MySpider(CrawlSpider):
    name = "huffpo"  # unique identifier for the spider
    allowed_domains = ['huffingtonpost.com']  # limits the crawl to this domain list
    start_urls = [
    'http://www.huffingtonpost.com/politics/'
    ]
    rules = [
        Rule(LinkExtractor(allow=r'/entry/'),
         callback='parse_item', follow=True)
    ]

    def parse_item(self, response):
        sel = Selector(response)
        results = []
        item = HuffpoItem()
        item['article_title'] = sel.xpath('//h1[@class="headline__title"]/text()').extract()
        #item['article_imagecaption'] = sel.xpath('//*[@id="article"]/div[1]/figure/figcaption/div[1]/p/text()').extract()
        item['article_author'] = sel.xpath('//div[@class="author-card__details"]/a/text()').extract()
        item['article_preview'] = sel.xpath('//h2[@class="headline__subtitle"]/text()').extract()
        #item['article_highlights'] = sel.xpath('.//div[@class="el__storyhighlights"]/ul/li/text()').extract()
        #item['article_edsource'] = sel.xpath('//*[@id="body-text"]/div[1]/div[2]/p/cite/text()').extract()
        item['article_content'] = sel.xpath('//div[@class="content-list-component text"]/p[descendant-or-self::text()]').extract()
        item['article_timestamp'] = sel.xpath('//div[@class="timestamp"]/span[1]/text()').extract()
        item['article_url'] = sel.xpath('/html/head/meta[8]/@content').extract()
        results.append(item)
        return results
