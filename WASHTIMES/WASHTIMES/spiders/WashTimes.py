import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from WASHTIMES.items import WashtimesItem  # item class 
from scrapy.selector import Selector


class MySpider(CrawlSpider):
    name = "washtimes"  # unique identifier for the spider
    allowed_domains = ['washingtontimes.com']  # limits the crawl to this domain list
    start_urls = [
    'http://www.washingtontimes.com/news/politics/'
    ]
    rules = [
        Rule(LinkExtractor(allow=r'/news/'),
         callback='parse_item', follow=True)
    ]

    def parse_item(self, response):
        sel = Selector(response)
        results = []
        item = WashtimesItem()
        item['article_title'] = sel.xpath('//h1[@class="page-headline"]/text()').extract()
        item['article_imagecaption'] = sel.xpath('//*[@id="content"]/div/div/section/article/div[1]/section/div/figure/figcaption/text()').extract()
        item['article_author'] = sel.xpath('//*[@id="content"]/div/div/section/article/div[3]/div[1]/span[1]/a/text()').extract()
        #item['article_preview'] = sel.xpath('//div[@class="content__standfirst"]/p/text()').extract()
        #item['article_highlights'] = sel.xpath('.//div[@class="el__storyhighlights"]/ul/li/text()').extract()
        #item['article_edsource'] = sel.xpath('//*[@id="article"]/div[2]/div/div[1]/div[2]/p[1]/text()').extract()
        item['article_content'] = sel.xpath('//div[@class="storyareawrapper"]/p[descendant-or-self::text()]').extract()
        item['article_timestamp'] = sel.xpath('//*[@id="content"]/div/div/section/article/div[3]/div[1]/span[2]/text()').extract()
        item['article_url'] = sel.xpath('/html/head/meta[21]/@content').extract()
        results.append(item)
        return results

