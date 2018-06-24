# -*- coding: utf-8 -*-
import scrapy
import datetime
import json
import requests
from scrapy.selector import Selector

class XkomSpider(scrapy.Spider):
    name = 'xkom'
    allowed_domains = ['x-kom.pl']
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
        
        offers = response.css(".product-detail-impression")

      #  print(response.request.url)

        best_price = offers[0].xpath('./@data-product-price').extract()

        object = yield {
                'productLinkId': self.link_dict[response.request.url],
				'price': float(best_price[0]),
				'timestamp': datetime.datetime.now() 
            }
        url2 = 'http://localhost:8095/scrap'
        response2 = requests.post(url2, data=object)