# -*- coding: utf-8 -*-
import scrapy
import datetime
import json
from scrapy.selector import Selector

class CeneoSpider(scrapy.Spider):
    name = 'ceneo'
    allowed_domains = ['ceneo.pl']
    with open('ceneo_links.json') as json_data:
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
        
        offers = response.css(".product-offer")

      #  print(response.request.url)

        best_price = offers[0].xpath('@data-price').extract()

        for offer in offers:
            if best_price > offer.xpath('@data-price').extract():
                best_price = offer.xpath('@data-price').extract()

        yield {
                'product_link_id': self.link_dict[response.request.url],
				'price': float(best_price[0]),
				'timestamp': datetime.datetime.now() 
            }