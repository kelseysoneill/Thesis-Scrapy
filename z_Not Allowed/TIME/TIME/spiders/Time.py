import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from TIME.items import TimeItem  # item class 
from scrapy.selector import Selector


class MySpider(CrawlSpider):
    name = "time"  # unique identifier for the spider
    allowed_domains = ['time.com']  # limits the crawl to this domain list
    start_urls = [
    'http://time.com/tag/2016-election/'
    ]
    rules = [
        Rule(LinkExtractor(allow=r'time.com/'),
         callback='parse_item', follow=True)
    ]

    def parse_item(self, response):
        sel = Selector(response)
        results = []
        item = TimeItem()
        item['article_title'] = sel.xpath('//h2[@class="article-title"]/text()').extract()
        item['article_imagecaption'] = sel.xpath('//*[@id="article-4205149"]/section/figure/figcaption/span[2]/text()').extract()
        item['article_author'] = sel.xpath('//span[@class="byline"]/a/text()').extract()
        #item['article_preview'] = sel.xpath('//div[@class="content__standfirst"]/p/text()').extract()
        #item['article_highlights'] = sel.xpath('.//div[@class="el__storyhighlights"]/ul/li/text()').extract()
        #item['article_edsource'] = sel.xpath('//*[@id="article"]/div[2]/div/div[1]/div[2]/p[1]/text()').extract()
        item['article_content'] = sel.xpath('//div[@class="message_content"]/p[descendant-or-self::text()]').extract()
        item['article_timestamp'] = sel.xpath('//*[@id="article-4205149"]/header/div/div[1]/time/@datetime').extract()
        item['article_url'] = sel.xpath('/html/head/meta[19]/@content').extract()
        results.append(item)
        return results

