
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item
from dmoz.items import DmozItem
from scrapy.spider import BaseSpider

import sys
import re

class DmozSpider(BaseSpider):
   name = "mountainproject"
   allowed_domains = ["mountainproject.com"]
   start_urls = [
    'http://mountainproject.com/v/whats-my-line/105738371'
    ]
    
    
   def parse(self, response):
       hxs = HtmlXPathSelector(response)
       sites = hxs.select('*')
       items = []
       for site in sites:
            item = DmozItem()
            item['monday'] = site.select('//*[@id="mpbox1085102004"]').extract()
#            item['tuesday'] = site.select('//*[@id="c59"]').extract()
#            item['wednesday'] = site.select('//*[@id="c58"]').extract()
#            item['thursday'] = site.select('//*[@id="c57"]').extract()
#            item['friday'] = site.select('//*[@id="c56"]').extract()
#            item['saturday'] = site.select('//*[@id="c55"]').extract()
#            item['sunday'] = site.select('//*[@id="c54"]').extract()
#            item['dificulty'] = site.select('//*[@id="Trail Level"]').extract()
#            item['star'] = site.select('').extract()
#            item['climb'] = site.select('').extract()
#            item['image'] = site.select('').extract()
#            item['rock'] = site.select('').extract()
            items = list(set(items))
            items.append(item)
            sorted(items, reverse=True)
            return items


'''
class DmozSpider(BaseSpider):
   name = "mountain"
   allowed_domains = ["mtbr.com"]
   start_urls = [
    'http://trails.mtbr.com/cat/united-states-trails/trails-arizona/PRD_455166_4513crx.aspx', 
    'http://trails.mtbr.com/cat/united-states-trails/trails-arizona/PRD_164472_4513crx.aspx', 
    'http://trails.mtbr.com/cat/united-states-trails/trails-arizona/PRD_367378_4513crx.aspx', 
    'http://trails.mtbr.com/cat/united-states-trails/trails-arizona/PRD_164473_4513crx.aspx', 
    'http://trails.mtbr.com/cat/united-states-trails/trails-arizona/PRD_164474_4513crx.aspx',
    'http://trails.mtbr.com/cat/united-states-trails/trails-arizona/PRD_412438_4513crx.aspx',
    'http://trails.mtbr.com/cat/united-states-trails/trails-arizona/PRD_337983_4513crx.aspx',
    'http://trails.mtbr.com/cat/united-states-trails/trails-arizona/PRD_164475_4513crx.aspx',
    'http://trails.mtbr.com/cat/united-states-trails/trails-arizona/PRD_408625_4513crx.aspx',
    'http://trails.mtbr.com/cat/united-states-trails/trails-arizona/PRD_164477_4513crx.aspx',
    'http://trails.mtbr.com/cat/united-states-trails/trails-arizona/PRD_368047_4513crx.aspx',
    'http://trails.mtbr.com/cat/united-states-trails/trails-arizona/PRD_440220_4513crx.aspx',
    'http://trails.mtbr.com/cat/united-states-trails/trails-arizona/PRD_164478_4513crx.aspx',
    'http://trails.mtbr.com/cat/united-states-trails/trails-arizona/PRD_366829_4513crx.aspx',
    'http://trails.mtbr.com/cat/united-states-trails/trails-arizona/PRD_366829_4513crx.aspx',
    'http://trails.mtbr.com/cat/united-states-trails/trails-arizona/PRD_164479_4513crx.aspx',
    'http://trails.mtbr.com/cat/united-states-trails/trails-arizona/PRD_164480_4513crx.aspx',
    'http://trails.mtbr.com/cat/united-states-trails/trails-arizona/PRD_366202_4513crx.aspx',
    'http://trails.mtbr.com/cat/united-states-trails/trails-arizona/PRD_449635_4513crx.aspx',
    'http://trails.mtbr.com/cat/united-states-trails/trails-arizona/PRD_164481_4513crx.aspx',
    'http://trails.mtbr.com/cat/united-states-trails/trails-arizona/PRD_348594_4513crx.aspx',
    'http://trails.mtbr.com/cat/united-states-trails/trails-arizona/PRD_164482_4513crx.aspx',
    'http://trails.mtbr.com/cat/united-states-trails/trails-arizona/PRD_164483_4513crx.aspx',
    'http://trails.mtbr.com/cat/united-states-trails/trails-arizona/PRD_367381_4513crx.aspx',
    'http://trails.mtbr.com/cat/united-states-trails/trails-arizona/PRD_348596_4513crx.aspx',
    'http://trails.mtbr.com/cat/united-states-trails/trails-arizona/PRD_451318_4513crx.aspx',
    'http://trails.mtbr.com/cat/united-states-trails/trails-arizona/PRD_428688_4513crx.aspx',
    'http://trails.mtbr.com/cat/united-states-trails/trails-arizona/PRD_348066_4513crx.aspx',
    'http://trails.mtbr.com/cat/united-states-trails/trails-arizona/PRD_164485_4513crx.aspx',
    'http://trails.mtbr.com/cat/united-states-trails/trails-arizona/PRD_164486_4513crx.aspx',
    'http://trails.mtbr.com/cat/united-states-trails/trails-arizona/PRD_164487_4513crx.aspx',
    'http://trails.mtbr.com/cat/united-states-trails/trails-arizona/PRD_164488_4513crx.aspx',
    'http://trails.mtbr.com/cat/united-states-trails/trails-arizona/PRD_164489_4513crx.aspx',
    'http://trails.mtbr.com/cat/united-states-trails/trails-arizona/PRD_424977_4513crx.aspx',
    'http://trails.mtbr.com/cat/united-states-trails/trails-arizona/PRD_164490_4513crx.aspx',
    'http://trails.mtbr.com/cat/united-states-trails/trails-arizona/PRD_437943_4513crx.aspx',
    'http://trails.mtbr.com/cat/united-states-trails/trails-arizona/PRD_164491_4513crx.aspx',
    'http://trails.mtbr.com/cat/united-states-trails/trails-arizona/PRD_364240_4513crx.aspx',
    'http://trails.mtbr.com/cat/united-states-trails/trails-arizona/PRD_288715_4513crx.aspx',
    'http://trails.mtbr.com/cat/united-states-trails/trails-arizona/PRD_164492_4513crx.aspx',
    'http://trails.mtbr.com/cat/united-states-trails/trails-arizona/PRD_171801_4513crx.aspx',
    'http://trails.mtbr.com/cat/united-states-trails/trails-arizona/PRD_424981_4513crx.aspx',
    'http://trails.mtbr.com/cat/united-states-trails/trails-arizona/PRD_164493_4513crx.aspx',
    'http://trails.mtbr.com/cat/united-states-trails/trails-arizona/PRD_164494_4513crx.aspx',
    'http://trails.mtbr.com/cat/united-states-trails/trails-arizona/PRD_366204_4513crx.aspx', 
    'http://trails.mtbr.com/cat/united-states-trails/trails-arizona/PRD_164496_4513crx.aspx'  #end of first page
   ]

   def parse(self, response):
       hxs = HtmlXPathSelector(response)
       sites = hxs.select('//ul/li')
       items = []
       for site in sites:
            item = DmozItem()
            item['latitude'] = site.select('//*[@id="Latitude"]').extract()
            item['longitude'] = site.select('//*[@id="Longitude"]').extract()
            item['name'] = site.select('//*[@id="productname"]/b').extract()
#            item['crag'] = site.select('').extract()
            item['trail_length'] = site.select('//*[@id="Trail Length"]').extract()
#            item['wall'] = site.select('').extract()
            item['location'] = site.select('//*[@id="City/County"]').extract()
            item['dificulty'] = site.select('//*[@id="Trail Level"]').extract()
#            item['star'] = site.select('').extract()
#            item['climb'] = site.select('').extract()
#            item['image'] = site.select('').extract()
#            item['rock'] = site.select('').extract()
            items = list(set(items))
            items.append(item)
            sorted(items, reverse=True)
            return items
'''
'''
#  class MulitPagesSpider(CrawlSpider):
class DmozSpider(CrawlSpider):
    name = 'multimount'
    allowed_domains = ['mtbr.com']
    start_url = ['http://trails.mtbr.com/cat/united-states-trails/trails-arizona/pls_4513crx.aspx']
    
    rules = (
        Rule(SgmlLinkExtractor(allow='trails.mtbr.com/cat/united-states-trails/trails-arizona/PRD_\d+\[6\].aspx'),
            'parse_category',
            follow=True,
        ),
    )    
    

    def parse_category(self, response):# parse_mulit because parse was def ^
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//ul/li') #what the fuck does this mean?
        items = []
        for site in sites:#should that be scrapted_items?
            item = DmozItem() 
            item['title'] = item.select('text()').extract()
#            item['longitude'] = site.select('//*[@id="Trail Length"]').extract()
#            item['name'] = site.select('//*[@id="productname"]/b').extract()
#            item['crag'] = site.select('').extract()
#            item['trail_length'] = site.select('//*[@id="Trail Length"]').extract()
#            item['wall'] = site.select('').extract()
#            item['location'] = site.select('//*[@id="City/County"]').extract()
#            item['dificulty'] = site.select('//*[@id="Trail Level"]').extract()
#            item['star'] = site.select('').extract()
#            item['climb'] = site.select('').extract()
#            item['image'] = site.select('').extract()
#            item['rock'] = site.select('').extract()
        items = list(set(items))
        items.append(item)
        return items
    
    rules = (
        Rule(SgmlLinkExtractor(allow='trails.mtbr.com/cat/united-states-trails/trails-arizona/[A-Z][a-zA-Z_/]+$'),
            'parse_category',
            follow=True,
        ),
    )
        
    rules = (
        Rule(SgmlLinkExtractor(allow='trails.mtbr.com/cat/united-states-trails/trails-arizona/PRD_\d+\[6\].aspx'),
            'parse_category',
            follow=True,
        ),
    )
'''  




