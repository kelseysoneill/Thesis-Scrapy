import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from WP.items import MyItem  # item class 
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector

class MySpider(CrawlSpider):
    name = "WPtest"  # unique identifier for the spider
    allowed_domains = ['washingtonpost.com']  # limits the crawl to this domain list
    start_urls = ['https://www.washingtonpost.com/politics/rand-paul-doubling-down-on-senate-presidential-bids-after-ky-elections/2015/11/03/0ff49922-8259-11e5-9afb-0c971f713d0c_story.html']  # first url to crawl in domain


    def parse(self, response):
        sel = Selector(response)
        results = []
        item = MyItem()
        item['a_title'] = sel.xpath('//div[@class="headline-kicker"]/h1[1]/text()').extract()

        results.append(item)
        return results
        
        