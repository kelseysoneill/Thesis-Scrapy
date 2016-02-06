import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from WP.items import MyItem  # item class 
from scrapy.selector import Selector


class MySpider(CrawlSpider):
    name = "WPcrawlpoll"  # unique identifier for the spider
    allowed_domains = ['washingtonpost.com']  # limits the crawl to this domain list
    start_urls = [
    'https://www.washingtonpost.com/news/the-fix/'
    ]
    rules = [
        Rule(LinkExtractor(allow=(r'contains:<polling>')), follow=True),
        Rule(LinkExtractor(), callback='parse_item')
        ]

    def parse_item(self, response):
        sel = Selector(response)
        results = []
        item = MyItem()
        item['article_title'] = sel.xpath('//*[@id="article-topper"]/h1/text()').extract()
        item['article_author1'] = sel.xpath('//*[@id="article-body"]/div[1]/span[1]/a/span/text()').extract()
        item['article_timestamp'] =sel.xpath('//*[@id="article-body"]/div[1]/span[2]/@content').extract()
        item['article_content'] = sel.xpath('//*[@id="article-body"]//text()').extract()
        item['article_url'] = sel.xpath('/html/head/meta[23]/@content').extract()
        results.append(item)
        return results

