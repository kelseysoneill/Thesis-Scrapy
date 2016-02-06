import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from CBSNEWS.items import CbsnewsItem  # item class 
from scrapy.selector import Selector



class MySpider(CrawlSpider):
    name = "CBS"  # unique identifier for the spider
    allowed_domains = ['cbsnews.com']  # limits the crawl to this domain list
    start_urls = [
    'http://www.cbsnews.com/election-2016/'
    ]
    rules = [
        Rule(LinkExtractor(allow=r'/news/'),
         callback='parse_item', follow=True)
    ]

    def parse_item(self, response):
        sel = Selector(response)
        results = []
        item = CbsnewsItem()
        item['article_title'] = sel.xpath('//h1[@class="title"]/text()').extract()
        item['article_imagecaption'] = sel.xpath('//*[@id="article"]/div[1]/figure/figcaption/div[1]/p/text()').extract()
        item['article_author'] = sel.xpath('//*[@id="article"]/header/div/span[2]/text()').extract()
        #item['article_preview'] = sel.xpath('.//div[@class="summary  "]/header/p[2]/text()').extract()
        #item['article_highlights'] = sel.xpath('.//div[@class="el__storyhighlights"]/ul/li/text()').extract()
        #item['article_edsource'] = sel.xpath('//*[@id="body-text"]/div[1]/div[2]/p/cite/text()').extract()
        item['article_content'] = sel.xpath('//div[@class="entry"]/p[descendant-or-self::text()]').extract()
        item['article_timestamp'] = sel.xpath('//*[@id="article"]/header/div/span[4]/text()').extract()
        item['article_url'] = sel.xpath('/html/head/meta[12]/@content').extract()
        results.append(item)
        return results
