# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item,Field

class MyItem(scrapy.Item):
    # define the data fields for the item (just one field used here)
    
    a_title = Field()
    b_author = Field()
    c_published = Field()
    d_content = Field() # paragraph content

    
    
