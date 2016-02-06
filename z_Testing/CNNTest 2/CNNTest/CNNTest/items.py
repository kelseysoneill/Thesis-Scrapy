# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item,Field

class MyItem(scrapy.Item):
    # define the data fields for the item (just one field used here)
    
    article_title = Field()
    article_author1 = Field()
    article_author2 = Field()
    article_author = Field()
    article_content = Field() # paragraph content
    article_timestamp = Field()
    article_highlights = Field()
    article_preview = Field()
    article_edsource = Field()
    article_url = Field()