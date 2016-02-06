import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from WP.items import MyItem  # item class 
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector

class MySpider(CrawlSpider):
    name = "WPnewsfix"  # unique identifier for the spider
    allowed_domains = ['washingtonpost.com']  # limits the crawl to this domain list
    start_urls = [
 'https://www.washingtonpost.com/news/the-fix',
 'https://www.washingtonpost.com/news/the-fix/wp/2015/09/27/john-boehners-sick-burn-of-ted-cruz-video/'
]

    def parse(self, response):
        sel = Selector(response)
        results = []
        item = MyItem()
        item['article_title'] = sel.xpath('//*[@id="article-topper"]/h1/text()').extract()
        item['article_author1'] = sel.xpath('//*[@class="pb-byline"]/a[1]/span[1]/text()').extract()
        item['article_author2'] = sel.xpath('//*[@class="pb-byline"]/a[2]/span[1]/text()').extract()
        item['article_timestamp'] =sel.xpath('//*[@id="article-body"]/div[1]/span[2]/@content').extract()
        item['article_content'] = sel.xpath('//*[@id="article-body"]/article/p/text()').extract()
        #item['e_sourceurl'] = sel.xpath('//*[@id="index-page"]/head/meta[24]/@content').extract()
        results.append(item)
        return results
