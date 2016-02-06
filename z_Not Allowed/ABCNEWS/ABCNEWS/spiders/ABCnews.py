import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ABCNEWS.items import AbcnewsItem  # item class 
from scrapy.selector import Selector



class MySpider(CrawlSpider):
    name = "ABCnews"  # unique identifier for the spider
    allowed_domains = ['abcnews.com','abcnews.go.com']  # limits the crawl to this domain list
    start_urls = [
    'http://abcnews.go.com/Politics/Election/'
    ]
    rules = [
        Rule(LinkExtractor(allow=r'/Politics/'),
         callback='parse_item', follow=True)
    ]

    def parse_item(self, response):
        sel = Selector(response)
        results = []
        item = AbcnewsItem()
        item['article_title'] = sel.xpath('//div[@class="container"]/header/h1/text()').extract()
        item['article_imagecaption'] = sel.xpath('//span[@class="caption"]/text()').extract()
        item['article_author'] = sel.xpath('//div[@class="article-meta"]/ul/li/div/text()').extract()
        #item['article_preview'] = sel.xpath('.//div[@class="summary  "]/header/p[2]/text()').extract()
        #item['article_highlights'] = sel.xpath('.//div[@class="el__storyhighlights"]/ul/li/text()').extract()
        #item['article_edsource'] = sel.xpath('//*[@id="body-text"]/div[1]/div[2]/p/cite/text()').extract()
        item['article_content'] = sel.xpath('//div[@class="article-copy"]/p[descendant-or-self::text()]')
        item['article_timestamp'] = sel.xpath('//*[@id="article-feed"]/article[1]/div/header/div/div/span/text()').extract()
        item['article_url'] = sel.xpath('/html/head/meta[16]/@content').extract()
        results.append(item)
        return results

notags = results.extract().replace('/<[^>]*>/g', ' ')

