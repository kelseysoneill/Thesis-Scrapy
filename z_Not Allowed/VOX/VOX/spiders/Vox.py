import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from VOX.items import VoxItem  # item class 
from scrapy.selector import Selector



class MySpider(CrawlSpider):
    name = "vox"  # unique identifier for the spider
    allowed_domains = ['vox.com']  # limits the crawl to this domain list
    start_urls = [
    'http://www.vox.com/2016/1/25/10831614/sanders-criticizes-clinton-for-supporting-iraq-war/'
    ]
    #rules = [
     #   Rule(LinkExtractor(allow=r'/us-news/'),
      #   callback='parse_item', follow=True)
    #]

    def parse(self, response):
        sel = Selector(response)
        results = []
        item = VoxItem()
        item['article_title'] = sel.xpath('//div[@class="l-container"]/div[1]/header/h2/text()').extract()
        #item['article_imagecaption'] = sel.xpath('//figure[@class="media-primary media-content()  "]/figcaption/text()').extract()
        #item['article_author'] = sel.xpath('//*[@id="article"]/div[2]/div/div[1]/div[2]/p[1]/span/a/span/text()').extract()
        #item['article_preview'] = sel.xpath('//div[@class="content__standfirst"]/p/text()').extract()
        #item['article_highlights'] = sel.xpath('.//div[@class="el__storyhighlights"]/ul/li/text()').extract()
        #item['article_edsource'] = sel.xpath('//*[@id="article"]/div[2]/div/div[1]/div[2]/p[1]/text()').extract()
        #item['article_content'] = sel.xpath('//div[@class="content__article-body from-content-api js-article__body"]/p[descendant-or-self::text()]').extract()
        #item['article_timestamp'] = sel.xpath('//*[@id="article"]/div[2]/div/div[1]/div[2]/p[2]/time[1]/@datetime').extract()
        #item['article_url'] = sel.xpath('//*[@id="js-context"]/head/meta[16]/@content').extract()
        results.append(item)
        return results