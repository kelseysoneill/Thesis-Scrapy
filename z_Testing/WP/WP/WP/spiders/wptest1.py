import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from WP.items import MyItem  # item class 
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector

class MySpider(CrawlSpider):
    name = "WPtest"  # unique identifier for the spider
    allowed_domains = ['washingtonpost.com']  # limits the crawl to this domain list
    start_urls = [
'https://www.washingtonpost.com/politics/rand-paul-doubling-down-on-senate-presidential-bids-after-ky-elections/2015/11/03/0ff49922-8259-11e5-9afb-0c971f713d0c_story.html',
'https://www.washingtonpost.com/politics/the-republican-field-has-a-new-target-marco-rubio/2015/11/03/9638d9cc-824e-11e5-8ba6-cec48b74b2a7_story.html',
'http://www.washingtonpost.com/politics/gop-candidates-expand-on-conservative-views-at-redstate-gathering/2015/08/08/acc2f286-3e01-11e5-9c2d-ed991d848c48_story.html',
'http://www.washingtonpost.com/politics/a-no-nonsense-approach-for-gop-candidate-carly-fiorina/2015/08/20/2bdc9eea-479f-11e5-846d-02792f854297_gallery.html',
'http://www.washingtonpost.com/politics/for-carly-fiorina-just-press-one-to-solve-the-nations-problems/2015/08/20/d553bfe4-4736-11e5-8ab4-c73967a143d3_story.html',
'http://www.washingtonpost.com/politics/after-months-of-obscurity-carly-fiorina-emerges-as-a-gop-contender/2015/08/07/52ed04fa-3d29-11e5-9c2d-ed991d848c48_story.html',
'http://www.washingtonpost.com/politics/in-haiti-rand-pauls-patients-are-happy-a-potential-donor-less-so/2015/08/19/3635fa3a-4696-11e5-8ab4-c73967a143d3_story.html',
'http://www.washingtonpost.com/politics/will-carly-fiorina-be-able-to-break-out-after-her-shining-debate-performance/2015/08/06/477c0de0-3c8a-11e5-8e98-115a3cf7d7ae_story.html',
'http://www.washingtonpost.com/politics/fading-in-the-polls-scott-walker-aims-to-attract-trump-voters/2015/08/18/48d0b900-45ab-11e5-846d-02792f854297_story.html',
'http://www.washingtonpost.com/politics/rand-paul-super-pac-head-indicted-on-2012-campaign-finance-charges/2015/08/05/9e21bb90-3b95-11e5-b3ac-8a79bc44e5e2_story.html',
'http://www.washingtonpost.com/politics/from-second-place-to-back-of-the-pack-santorum-fails-to-gain-2016-traction/2015/08/05/df9afa98-3b89-11e5-b3ac-8a79bc44e5e2_story.html',
'http://www.washingtonpost.com/politics/bill-clinton-called-donald-trump-ahead-of-republicans-2016-launch/2015/08/05/e2b30bb8-3ae3-11e5-b3ac-8a79bc44e5e2_story.html',
'http://www.washingtonpost.com/politics/donald-trump-hillary-clinton-and-chaos-visit-the-iowa-state-fair/2015/08/15/295e4150-42d6-11e5-8ab4-c73967a143d3_story.html',
'http://www.washingtonpost.com/politics/as-debate-looms-rand-paul-sees-a-chance-to-be-the-gop-dove/2015/08/02/f1b4450e-3927-11e5-8e98-115a3cf7d7ae_story.html',
'http://www.washingtonpost.com/politics/why-donald-trump-makes-sense-to-a-lot-of-voters--even-some-democrats/2015/08/15/cee648f0-42bf-11e5-8ab4-c73967a143d3_story.html',
'http://www.washingtonpost.com/politics/what-kind-of-party-will-the-republican-nominee-lead-in-2016/2015/08/01/9f14a3ea-37d1-11e5-b673-1df005a0fb28_story.html',
'http://www.washingtonpost.com/politics/million-dollar-donors-pump-huge-sums-into-2016-white-house-race/2015/07/31/e2befec4-37b8-11e5-9739-170df8af8eb9_story.html',
'http://www.washingtonpost.com/politics/ben-carson-riding-a-fresh-surge-in-the-polls-braces-for-his-close-up/2015/08/13/91472e44-4204-11e5-8e7d-9c033e6745d8_story.html',
'http://www.washingtonpost.com/politics/scott-walker-approves-spending-250-million-on-milwaukee-bucks-arena/2015/08/12/5cd72d54-4055-11e5-9561-4b3dc93e3b9a_story.html'
'http://www.washingtonpost.com/politics/jeb-bush-faults-hillary-clinton-for-premature-iraq-withdrawal/2015/08/11/ffa3e2a6-4042-11e5-9561-4b3dc93e3b9a_story.html'
]

    def parse(self, response):
        sel = Selector(response)
        results = []
        item = MyItem()
        item['a_title'] = sel.xpath('//*[@id="article-topper"]/h1/text()').extract()
        item['b_author1'] = sel.xpath('//*[@id="article-body"]/div[2]/span[1]/a[1]/span/text()').extract()
        item['b_author2'] = sel.xpath('//*[@id="article-body"]/div[2]/span[1]/a[2]/span/text()').extract()
        item['c_published'] =sel.xpath('//*[@id="article-body"]/div[2]/span[2]/@content').extract()
        item['d_content'] = sel.xpath('//*[@id="article-body"]/article/p/text()').extract()
        results.append(item)
        return results
