# -*- coding: utf-8 -*-
import scrapy
import datetime
import json
import requests
from scrapy.selector import Selector

class CeneoSpider(scrapy.Spider):
    name = 'ceneo'
    allowed_domains = ['ceneo.pl']
    url = 'http://localhost:8095/scrap'
    data = '''{
    "domain": "string",
    "links": [
    {
        "link": "string",
        "productLinkId": "string"
    }
}'''
    response = requests.get(url, data=data)
    print(response.json())
    for object in response.json():
        if object['domain'] == allowed_domains[0]:
            links = object['links']
    link_dict = {}
    for data in links:
        link_dict[data['link']] = data['productLinkId']
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

        object = yield {
                'productLinkId': self.link_dict[response.request.url],
				'price': float(best_price[0]),
				'timestamp': datetime.datetime.now() 
            }
        url2 = 'http://localhost:8095/scrap'
        response2 = requests.post(url2, data=object)