# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item,Field

class MyItem(scrapy.Item):
    # define the data fields for the item (just one field used here)
    
    a_in_title = Field()
    b_out_title = Field()
    c_excerpt = Field() # paragraph content
    d_published = Field()
    e_category = Field()
    f_tag = Field()
    
    
