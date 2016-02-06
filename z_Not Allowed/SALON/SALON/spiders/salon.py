import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from SALON.items import SalonItem  # item class 
from scrapy.selector import Selector



class MySpider(CrawlSpider):
    name = "saloncrawl"  # unique identifier for the spider
    allowed_domains = ['salon.com']  # limits the crawl to this domain list
    start_urls = [
    'http://www.salon.com/2016/02/03/3_million_reasons_why_hillary_should_be_nervous_grassroots_sanders_supporters_send_message_with_deluge_of_donations_after_iowa/'
    ]
   # rules = [
    #    Rule(LinkExtractor(allow=r'/msnbc/'),
     #    callback='parse_item', follow=True)
    #]

    def parse(self, response):
        sel = Selector(response)
        results = []
        item = SalonItem()
        item['article_title'] = sel.xpath('//h1[@class="is-title-pane panel-pane pane-node-title"]/text()').extract()
        #item['article_imagecaption'] = sel.xpath('//div[@class="media-meta__caption"]/text()').extract()
        #item['article_author'] = sel.xpath('//*[@id="block-system-main"]/div/div/article/div/div[2]/span[2]/text()').extract()
        #item['article_preview'] = sel.xpath('//div[@class="content__standfirst"]/p/text()').extract()
        #item['article_highlights'] = sel.xpath('.//div[@class="el__storyhighlights"]/ul/li/text()').extract()
        #item['article_edsource'] = sel.xpath('//*[@id="article"]/div[2]/div/div[1]/div[2]/p[1]/text()').extract()
        #item['article_content'] = sel.xpath('//div[@class="field field-name-body field-type-text-with-summary field-label-hidden"]/p[descendant-or-self::text()]').extract()
        #item['article_timestamp'] = sel.xpath('//*[@id="block-system-main"]/div/div/article/header/div[3]/time/@datetime').extract()
        #item['article_url'] = sel.xpath('/html/head/meta[4]/@content').extract()
        results.append(item)
        return results
