import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from NewsAggregators.items import MyItem  # item class 
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector

class MySpider(CrawlSpider):
    name = "CS2"  # unique identifier for the spider
    allowed_domains = ['campaignspeak.com']  # limits the crawl to this domain list
    start_urls = ['http://www.campaignspeak.com/']  # first url to crawl in domain

    rules = (Rule (LinkExtractor(), callback="parse", follow=True),)


    def parse(self, response):
        sel = Selector(response)
        articles = sel.xpath('//article')
        results = []

        for articles in articles:
            item = MyItem()
            item['a_in_title'] = articles.xpath('.//div[@class="post-right"]/h2/a[1]').extract()
            item['b_out_title'] = articles.xpath('.//div[@class="post-right"]/h2/a[2]').extract()
            item['c_excerpt'] = articles.xpath('.//div[@class="entry-content"]/text()').extract()
            item['d_published'] = articles.xpath('.//div[@class="post-right"]/div[1]/span[4]/text()').extract()
            item['e_category'] = articles.xpath('.//div/div[1]/span[5]/a/text()').extract()
            results.append(item)
        return results