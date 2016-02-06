import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from USATODAY.items import UsatodayItem  # item class 
from scrapy.selector import Selector



class MySpider(CrawlSpider):
    name = "USAtoday"  # unique identifier for the spider
    allowed_domains = ['usatoday.com']  # limits the crawl to this domain list
    start_urls = [
    'http://www.usatoday.com/story/news/politics/onpolitics/2016/02/02/bernie-sanders-not-conceding-iowa/79717232/'
    ]
    #rules = [
     #   Rule(LinkExtractor(allow=r'/politics/2016-election/'),
      #   callback='parse_item', follow=True)
    #]


    def parse(self, response):
        sel = Selector(response)
        results = []
        item = UsatodayItem()
        item['article_title'] = sel.xpath('//h1[@class="asset-headline"]/text()').extract()
        #item['article_title'] = sel.xpath('.//section[@class="blogtopbar-bucket story-headline-module story-story-headline-module"]/hl/text()').extract()
        #item['article_imagecaption'] = sel.xpath('//*[@id="globalWrapper"]/main/div[4]/div/article/div[1]/section[1]/div/div/figure/figcaption/p/text()').extract()
        item['article_author'] = sel.xpath('//*[@id="module-position-Ox0OX0TasAM"]/div/span[1]/text()').extract()
        #item['article_preview'] = sel.xpath('.//div[@class="summary  "]/header/p[2]/text()').extract()
       #item['article_highlights'] = sel.xpath('.//div[@class="el__storyhighlights"]/ul/li/text()').extract()
        #item['article_edsource'] = sel.xpath('//*[@id="body-text"]/div[1]/div[2]/p/cite/text()').extract()
        #item['article_content'] = sel.xpath('.//div[@class="article-body"]/p/text()').extract()
        #item['article_timestamp'] = sel.xpath('.//div[@class="article-flags"]/div[1]/div[2]/time/@datetime').extract()
        #item['article_url'] = sel.xpath('/html/head/meta[9]/@content').extract()
        results.append(item)
        return results