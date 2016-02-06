import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from BBC.items import BbcItem  # item class 
from scrapy.selector import Selector



class MySpider(CrawlSpider):
    name = "bbc"  # unique identifier for the spider
    allowed_domains = ['bbc.com']  # limits the crawl to this domain list
    start_urls = [
    'http://www.bbc.com/news/election/us2016'
    ]
    rules = [
        Rule(LinkExtractor(allow=r'world-us'),
         callback='parse_item', follow=True)
    ]

    def parse_item(self, response):
        sel = Selector(response)
        results = []
        item = BbcItem()
        item['article_title'] = sel.xpath('//h1[@class="story-body__h1"]/text()').extract()
        item['article_imagecaption'] = sel.xpath('//figure[@class="media-landscape has-caption full-width"]/figcaption/span[2]/text()').extract()
        item['article_author'] = sel.xpath('//div[@class="byline__name-and-title"]/a/span/text()').extract()
        #item['article_preview'] = sel.xpath('//p[@class="story-body__introduction"]/text()').extract()
        #item['article_highlights'] = sel.xpath('.//div[@class="el__storyhighlights"]/ul/li/text()').extract()
        #item['article_edsource'] = sel.xpath('//*[@id="article"]/div[2]/div/div[1]/div[2]/p[1]/text()').extract()
        item['article_content'] = sel.xpath('//div[@class="story-body__inner"]/p[descendant-or-self::text()]').extract()
        item['article_timestamp'] = sel.xpath('//div[@class="story-body__mini-info-list-and-share"]/ul/li/div/text()').extract()
        item['article_url'] = sel.xpath('//*[@id="responsive-news"]/head/meta[15]/@content').extract()
        results.append(item)
        return results
