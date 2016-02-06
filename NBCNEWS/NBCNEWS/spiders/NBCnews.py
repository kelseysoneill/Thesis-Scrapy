import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from NBCNEWS.items import NbcnewsItem  # item class 
from scrapy.selector import Selector



class MySpider(CrawlSpider):
    name = "NBC"  # unique identifier for the spider
    allowed_domains = ['nbcnews.com']  # limits the crawl to this domain list
    start_urls = [
    'http://www.nbcnews.com/politics/2016-election/'
    ]
    rules = [
        Rule(LinkExtractor(allow=r'/politics/2016-election/'),
         callback='parse_item', follow=True)
    ]


    def parse_item(self, response):
        sel = Selector(response)
        results = []
        item = NbcnewsItem()
        item['article_title'] = sel.xpath('.//div[@class="article-hed"]/h1/text()').extract()
        #item['article_imagecaption'] = sel.xpath('//*[@id="globalWrapper"]/main/div[4]/div/article/div[1]/section[1]/div/div/figure/figcaption/p/text()').extract()
        item['article_author'] = sel.xpath('//*[@id="510171"]/div/div[1]/header/div[2]/p/span/span[2]/text()').extract()
        #item['article_preview'] = sel.xpath('.//div[@class="summary  "]/header/p[2]/text()').extract()
        #item['article_highlights'] = sel.xpath('.//div[@class="el__storyhighlights"]/ul/li/text()').extract()
        #item['article_edsource'] = sel.xpath('//*[@id="body-text"]/div[1]/div[2]/p/cite/text()').extract()
        item['article_content'] = sel.xpath('.//div[@class="article-body"]/p/text()').extract()
        item['article_timestamp'] = sel.xpath('.//div[@class="article-flags"]/div[1]/div[2]/time/@datetime').extract()
        item['article_url'] = sel.xpath('/html/head/meta[9]/@content').extract()
        results.append(item)
        return results