import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from FOX.items import FoxItem  # item class 
from scrapy.selector import Selector


class MySpider(CrawlSpider):
    name = "FOXitem"  # unique identifier for the spider
    allowed_domains = ['foxnews.com']  # limits the crawl to this domain list
    start_urls = [
    'http://www.foxnews.com/politics/elections/2016/presidential-election-headquarters'
    ]
    rules = [
        Rule(LinkExtractor(allow=r'/politics/'),
         callback='parse_item', follow=True)
    ]

    def parse_item(self, response):
        sel = Selector(response)
        results = []
        item = FoxItem()
        item['article_title'] = sel.xpath('//div[@class="main"]/article/div/h1/text()').extract()
        #item['article_imagecaption'] = sel.xpath('.//div[@class="entry-content"]/div[3]/figure[1]/figcaption[1]/span[1]/text()').extract()
        item['article_author'] = sel.xpath('.//div[@class="article-info"]/div/div/a/text()').extract()
        #item['article_highlights'] = sel.xpath('.//div[@class="el__storyhighlights"]/ul/li/text()').extract()
        #item['article_edsource'] = sel.xpath('//*[@id="body-text"]/div[1]/div[2]/p/cite/text()').extract()
        item['article_content'] = sel.xpath('.//div[@class="article-text"]/p[descendant-or-self::text()]').extract()
        item['article_timestamp'] = sel.xpath('.//div[@class="article-info"]/div/time/@datetime').extract()
        item['article_url'] = sel.xpath('/html/head/meta[30]/@content').extract()
        results.append(item)
        return results
