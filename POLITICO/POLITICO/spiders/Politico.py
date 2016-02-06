import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from POLITICO.items import PoliticoItem  # item class 
from scrapy.selector import Selector



class MySpider(CrawlSpider):
    name = "politico"  # unique identifier for the spider
    allowed_domains = ['politico.com']  # limits the crawl to this domain list
    start_urls = [
    'http://www.politico.com/news/2016-elections'
    ]
    rules = [
        Rule(LinkExtractor(allow=r'/story/'),
         callback='parse_item', follow=True)
    ]


    def parse_item(self, response):
        sel = Selector(response)
        results = []
        item = PoliticoItem()
        item['article_title'] = sel.xpath('.//h1[@class=" "]/text()').extract()
        item['article_imagecaption'] = sel.xpath('//*[@id="globalWrapper"]/main/div[4]/div/article/div[1]/section[1]/div/div/figure/figcaption/p/text()').extract()
        item['article_author'] = sel.xpath('.//div[@class="summary  "]/footer/p/span/a/text()').extract()
        item['article_preview'] = sel.xpath('.//div[@class="summary  "]/header/p[2]/text()').extract()
        #item['article_highlights'] = sel.xpath('.//div[@class="el__storyhighlights"]/ul/li/text()').extract()
        #item['article_edsource'] = sel.xpath('//*[@id="body-text"]/div[1]/div[2]/p/cite/text()').extract()
        item['article_content'] = sel.xpath('.//div[@class="content-group story-core"]//text()').extract()
        item['article_timestamp'] = sel.xpath('.//div[@class="summary  "]/footer/p[2]/time/@datetime').extract()
        item['article_url'] = sel.xpath('/html/head/link[2]/@href').extract()
        results.append(item)
        return results

