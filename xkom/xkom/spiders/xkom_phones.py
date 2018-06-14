# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector

class XkomSpider(scrapy.Spider):
    name = 'xkom'
    allowed_domains = ['x-kom.pl']
    with open('xkom_links.json') as json_data:
        links = json.load(json_data)
   # print(links)
    link_dict = {}
    for data in links:
        link_dict[data['link']] = data['id']
    #print(link_dict)
    #print(link_dict.keys())
    start_urls = link_dict.keys()

    def parse(self, response):
        #response.css('tr').xpath('@data-price').extract()
        
        offers = response.css(".product-detail-impression")

      #  print(response.request.url)

        best_price = offers[0].xpath('./@data-product-price').extract()

        yield {
                'product_link_id': self.link_dict[response.request.url],
				'price': float(best_price[0]),
				'timestamp': datetime.datetime.now() 
            }