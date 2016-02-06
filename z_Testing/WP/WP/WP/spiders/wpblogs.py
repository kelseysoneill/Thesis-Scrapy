import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from WP.items import MyItem  # item class 
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector

class MySpider(CrawlSpider):
    name = "WPblogs"  # unique identifier for the spider
    allowed_domains = ['washingtonpost.com']  # limits the crawl to this domain list
    start_urls = [
'https://www.washingtonpost.com/blogs/right-turn/wp/2015/11/04/whats-next-for-the-struggling-jeb-bush/',
 'https://www.washingtonpost.com/blogs/plum-line/wp/2015/11/03/donald-trump-turns-his-buzz-saw-towards-marco-rubio/',
 'https://www.washingtonpost.com/blogs/right-turn/wp/2015/10/23/will-donald-trump-stick-around-to-lose-in-iowa/',
 'https://www.washingtonpost.com/blogs/right-turn/wp/2015/10/23/rubio-and-bush-make-the-case-against-clinton/',
 'http://www.washingtonpost.com/blogs/post-partisan/wp/2015/10/21/the-insiders-bush-kasich-and-rubio-are-stronger-than-you-think/',
 'https://www.washingtonpost.com/blogs/plum-line/wp/2015/10/20/are-republican-voters-going-to-come-to-their-senses-about-donald-trump/',
 'https://www.washingtonpost.com/blogs/right-turn/wp/2015/10/20/jeb-bushs-big-chance-to-knock-out-donald-trump/',
 'https://www.washingtonpost.com/blogs/capital-weather-gang/wp/2015/10/19/no-donald-trump-the-existence-of-fall-does-not-disprove-global-warming/',
 'http://www.washingtonpost.com/blogs/plum-line/wp/2015/10/30/marco-rubios-claim-that-hillary-lied-about-benghazi-debunked/',
 'http://www.washingtonpost.com/blogs/post-partisan/wp/2015/10/29/john-kasich-calls-out-the-gop-field/',
 'https://www.washingtonpost.com/blogs/erik-wemple/wp/2015/10/15/donald-trump-now-officially-owns-cable-news/',
 'https://www.washingtonpost.com/blogs/right-turn/wp/2015/10/15/rubio-adds-to-his-momentum/',
 'https://www.washingtonpost.com/blogs/erik-wemple/wp/2015/09/27/now-ben-carsons-blaming-the-media-for-his-comment-about-muslims/',
 'https://www.washingtonpost.com/blogs/erik-wemple/wp/2015/10/14/cable-news-debate-ratings-destroy-american-political-cliche/',
 'https://www.washingtonpost.com/blogs/right-turn/wp/2015/10/14/a-rocky-october-for-donald-trump/',
 'https://www.washingtonpost.com/blogs/erik-wemple/wp/2015/10/13/fox-newss-shepard-smith-gores-nbc-for-drafting-donald-trump-to-host-snl/',
 'https://www.washingtonpost.com/blogs/right-turn/wp/2015/10/13/iowa-eliminates-new-hampshire-selects/',
 'https://www.washingtonpost.com/blogs/plum-line/wp/2015/09/25/marco-rubio-knows-how-to-take-on-donald-trump-jeb-bush-doesnt/',
 'https://www.washingtonpost.com/blogs/all-opinions-are-local/wp/2015/10/13/virginia-for-the-win-kasichs-richmond-event-may-sink-him/',
 'http://www.washingtonpost.com/blogs/fact-checker/wp/2015/09/25/carly-fiorinas-bogus-secretary-to-ceo-career-trajectory-fact-checker-biography/',
 'https://www.washingtonpost.com/blogs/right-turn/wp/2015/10/12/ted-cruzs-cynical-appeal/',
 'https://www.washingtonpost.com/blogs/achenblog/wp/2015/09/24/this-blog-item-will-not-be-trending/',
 'https://www.washingtonpost.com/blogs/right-turn/wp/2015/09/24/marco-rubios-moment-2/',
 'https://www.washingtonpost.com/blogs/plum-line/wp/2015/09/24/morning-plum-no-donald-trump-isnt-really-telling-it-like-it-is/',
 'https://www.washingtonpost.com/blogs/erik-wemple/wp/2015/09/23/big-news-donald-trump-boycotting-fox-news/',
 'https://www.washingtonpost.com/blogs/plum-line/wp/2015/09/23/why-the-gop-race-might-come-down-to-marco-rubio-versus-jeb-bush/',
 'https://www.washingtonpost.com/blogs/plum-line/wp/2015/09/23/morning-plum-the-pope-donald-trump-and-the-gop-paradox/',
 'https://www.washingtonpost.com/blogs/monkey-cage/wp/2015/10/11/which-republican-presidential-candidate-will-drop-out-next-maybe-these-two/',
 'http://www.washingtonpost.com/blogs/post-partisan/wp/2015/09/22/the-insiders-what-we-learn-from-perrys-and-walkers-exits/',
 'https://www.washingtonpost.com/blogs/compost/wp/2015/09/21/scott-walker-leaves-the-race-with-one-of-the-worst-political-euphemisms-yet/',
 'https://www.washingtonpost.com/blogs/right-turn/wp/2015/10/09/is-it-do-or-die-time-for-marco-rubio/',
 'http://www.washingtonpost.com/blogs/fact-checker/wp/2015/09/21/scott-walker-biography-the-complete-collection/',
 'http://www.washingtonpost.com/blogs/monkey-cage/wp/2015/09/21/if-you-think-super-pacs-have-changed-everything-about-the-presidential-primary-think-again/',
 'https://www.washingtonpost.com/blogs/fact-checker/wp/2015/10/09/john-kasichs-claim-that-there-was-a-5-trillion-surplus-when-he-left-washington-in-2001-fact-checker-biography/',
 'https://www.washingtonpost.com/blogs/compost/wp/2015/10/08/okay-sure-donald-trump-for-speaker/',
 'https://www.washingtonpost.com/blogs/right-turn/wp/2015/10/07/why-is-john-kasich-down-and-chris-christie-up/',
 'https://www.washingtonpost.com/blogs/plum-line/wp/2015/09/01/donald-trump-reveals-where-the-real-conflict-within-the-gop-lies/',
 'http://www.washingtonpost.com/blogs/fact-checker/wp/2015/09/01/rand-pauls-grand-inaccurate-retelling-of-federal-swat-team-raids/',
 'https://www.washingtonpost.com/blogs/right-turn/wp/2015/08/31/who-rises-as-walker-falls/',
 'http://www.washingtonpost.com/blogs/fact-checker/wp/2015/08/31/cruzs-claim-that-the-administration-policy-led-to-the-release-of-104000-violent-criminal-aliens/',
 'https://www.washingtonpost.com/blogs/right-turn/wp/2015/08/30/kasich-vs-defense-hawks-on-pentagon-budget/',
 'https://www.washingtonpost.com/blogs/right-turn/wp/2015/08/28/cnns-phony-excuse-to-keep-fiorina-out-of-the-debate/',
 'http://www.washingtonpost.com/blogs/fact-checker/wp/2015/09/18/marco-rubios-claim-that-north-korea-has-dozens-of-nukes-and-can-strike-california/',
 'http://www.washingtonpost.com/blogs/post-partisan/wp/2015/09/17/poor-rand-paul/',
 'https://www.washingtonpost.com/blogs/right-turn/wp/2015/09/17/fresh-from-a-debate-win-lindsey-graham-goes-after-trump-kasich/',
 'https://www.washingtonpost.com/blogs/right-turn/wp/2015/09/07/walkers-search-for-authenticity/',
 'https://www.washingtonpost.com/blogs/right-turn/wp/2015/08/27/walker-shouldnt-waste-his-opportunity-on-foreign-policy/',
 'http://www.washingtonpost.com/blogs/fact-checker/wp/2015/09/16/scott-walkers-sweeping-label-of-wisconsin-as-a-blue-state-fact-checker-biography/',
 'https://www.washingtonpost.com/blogs/right-turn/wp/2015/09/06/pro-israel-conservatives-reject-merely-policing-the-iran-deal/',
 'https://www.washingtonpost.com/blogs/answer-sheet/wp/2015/09/16/once-again-gov-scott-walker-ignores-teacher-who-wants-him-to-stop-talking-about-her/',
 'https://www.washingtonpost.com/blogs/right-turn/wp/2015/08/26/carly-fiorinas-smart-debate-gambit/',
 'https://www.washingtonpost.com/blogs/plum-line/wp/2015/08/26/marco-rubio-eliminating-the-capital-gains-tax-will-help-bartenders-like-my-father/',
 'http://www.washingtonpost.com/blogs/fact-checker/wp/2015/09/15/scott-walkers-exaggerated-claims-of-employment-trends-in-wisconsin-fact-checker-biography/',
 'https://www.washingtonpost.com/blogs/plum-line/wp/2015/09/15/morning-plum-donald-trump-is-in-on-the-joke-and-the-jokes-on-you/',
 'https://www.washingtonpost.com/blogs/right-turn/wp/2015/08/26/trump-and-the-early-state-problem/',
 'https://www.washingtonpost.com/blogs/plum-line/wp/2015/09/14/scott-walkers-race-to-the-bottom/',
 'http://www.washingtonpost.com/blogs/fact-checker/wp/2015/09/14/scott-walker-inaccurately-takes-credit-for-inspiring-the-occupy-movement-fact-checker-biography/',
 'https://www.washingtonpost.com/blogs/right-turn/wp/2015/09/13/perry-exits-a-sad-sign-of-our-politics/',
 'https://www.washingtonpost.com/blogs/plum-line/wp/2015/09/03/donald-trump-snookers-the-gop-establishment-again/',
 'https://www.washingtonpost.com/blogs/plum-line/wp/2015/08/24/morning-plum-how-donald-trump-has-unmasked-his-gop-rivals/',
 'https://www.washingtonpost.com/blogs/plum-line/wp/2015/09/11/the-gops-donald-trump-nightmare-may-soon-get-a-whole-lot-worse/',
 'https://www.washingtonpost.com/blogs/plum-line/wp/2015/08/21/decoding-scott-walkers-dodge-on-birthright-citizenship/',
 'https://www.washingtonpost.com/blogs/erik-wemple/wp/2015/09/10/cnn-stretches-the-debate-field-accommodating-carly-fiorina/',
 'https://www.washingtonpost.com/blogs/plum-line/wp/2015/09/02/morning-plum-donald-trumps-supporters-want-mass-deportations-new-poll-finds/',
 'https://www.washingtonpost.com/blogs/plum-line/wp/2015/09/10/scott-walker-vows-to-wreak-havoc-on-washington-as-if-that-would-be-a-good-thing/',
 'http://www.washingtonpost.com/blogs/fact-checker/wp/2015/08/21/rick-perrys-apples-to-oranges-boast-of-texas-graduation-rates/',
 'http://www.washingtonpost.com/blogs/answer-sheet/wp/2015/08/08/white-house-was-grateful-to-jeb-bush-for-helping-with-common-core-says-former-obama-aide/',
 'https://www.washingtonpost.com/blogs/right-turn/wp/2015/08/20/john-kasich-talks-to-right-turn/',
 'http://www.washingtonpost.com/blogs/post-partisan/wp/2015/08/07/marco-rubio-and-carly-fiorina-win-the-republican-debate/',
 'http://www.washingtonpost.com/blogs/answer-sheet/wp/2015/08/19/kasich-if-i-were-king-in-america-i-would-abolish-all-teachers-lounges-where-they-sit-together-and-worry-about-how-woe-is-us/',
 'https://www.washingtonpost.com/blogs/right-turn/wp/2015/08/19/kasich-understands-how-to-run-in-a-trump-world/',
 'https://www.washingtonpost.com/blogs/right-turn/wp/2015/08/19/scott-walker-goes-wobbly/',
 'https://www.washingtonpost.com/blogs/right-turn/wp/2015/08/17/how-to-tackle-policy-in-a-presidential-campaign/',
 'https://www.washingtonpost.com/blogs/right-turn/wp/2015/08/05/if-scott-walker-wins-it-will-be-because/',
 'http://www.washingtonpost.com/blogs/answer-sheet/wp/2015/08/04/teacher-to-chris-christie-heres-my-face-go-ahead-and-punch-it/',
 'http://www.washingtonpost.com/blogs/post-partisan/wp/2015/07/31/these-two-quotes-from-n-h-show-the-war-raging-within-the-republican-party/',
 'http://www.washingtonpost.com/blogs/post-partisan/wp/2015/07/30/marco-rubio-is-in-trouble/',
 'https://www.washingtonpost.com/blogs/plum-line/wp/2015/07/29/scott-walker-gets-a-taste-of-philadelphia-cheesestake-politics/',
 'http://www.washingtonpost.com/blogs/answer-sheet/wp/2015/08/11/wisconsin-principals-tell-scott-walker-stop-hurting-our-schools/',
 'http://www.washingtonpost.com/blogs/fact-checker/wp/2015/08/10/rubios-fantasy-figure-on-bank-closures-due-to-dodd-frank/',
 'http://www.washingtonpost.com/blogs/post-politics/wp/2015/07/19/george-h-w-bush-discharged-from-hospital/',
 'http://www.washingtonpost.com/blogs/right-turn/wp/2015/07/19/how-to-handle-a-bully-like-trump/',
 'http://www.washingtonpost.com/blogs/answer-sheet/wp/2015/07/19/how-clinton-sanders-omalley-answer-unions-questions-about-education/',
 'http://www.washingtonpost.com/blogs/the-fix/wp/2015/07/19/bernie-sanders-newest-fan-jesse-ventura/',
 'http://www.washingtonpost.com/blogs/post-politics/wp/2015/07/18/hillary-clinton-slams-trump-over-mccain-comments/',
 'http://www.washingtonpost.com/blogs/post-politics/wp/2015/07/17/scott-walker-americans-want-action-in-washington-more-than-bipartisanship/',
 'http://www.washingtonpost.com/blogs/post-politics/wp/2015/07/16/snapchat-steps-into-2016-campaign-with-iowa-live-story-and-kasich-walker-ads/',
 'http://www.washingtonpost.com/blogs/post-politics/wp/2015/07/16/scott-walker-wants-you-to-know-he-still-loves-harleys/',
 'http://www.washingtonpost.com/blogs/the-fix/wp/2015/07/16/donald-trump-now-thinks-john-mccain-who-he-called-very-bright-in-2008-is-a-dummy/',
 'http://www.washingtonpost.com/blogs/the-fix/wp/2015/07/16/heres-how-hillary-clinton-knows-that-61-percent-of-her-donors-were-women/',
 'http://www.washingtonpost.com/blogs/the-fix/wp/2015/07/16/this-isnt-a-good-trend-line-for-hillary-clintons-2016-prospects/',
 'http://www.washingtonpost.com/blogs/the-fix/wp/2015/07/16/where-the-2016-candidates-raised-their-money-in-8-maps/',
 'http://www.washingtonpost.com/blogs/the-fix/wp/2015/07/16/bernie-sanderss-limited-appeal-even-to-democrats/',
 'http://www.washingtonpost.com/blogs/post-politics/wp/2015/07/15/female-donors-help-hillary-clinton-bring-in-47-5-million-in-second-quarter/',
 'http://www.washingtonpost.com/blogs/post-politics/wp/2015/07/15/the-bernie-sanders-campaign-brought-to-you-by-small-dollar-donors/',
 'http://www.washingtonpost.com/blogs/the-fix/wp/2015/07/15/the-fallacy-of-the-real-hillary-clinton/'
 ]


    def parse(self, response):
        sel = Selector(response)
        results = []
        item = MyItem()
        item['a_title'] = sel.xpath('//*[@id="article-topper"]/h1/text()').extract()
        item['b_author1'] = sel.xpath('//*[@class="pb-byline"]/a[1]/span[1]/text()').extract()
        item['b_author2'] = sel.xpath('//*[@class="pb-byline"]/a[2]/span[1]/text()').extract()
        item['c_published'] =sel.xpath('//*[@id="article-body"]/div[1]/span[2]/@content').extract()
        item['d_content'] = sel.xpath('//*[@id="article-body"]/article/p/text()').extract()
        #item['e_sourceurl'] = sel.xpath('//*[@id="index-page"]/head/meta[24]/@content').extract()
        results.append(item)
        return results
