# -*- coding: utf-8 -*-
import scrapy
import datetime
import json
import requests
from scrapy.selector import Selector


class NeonetSpider(scrapy.Spider):
    name = 'neonet'
    allowed_domains = ['neonet.pl']
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

    start_urls = link_dict.keys()

    def parse(self, response):

        best_price = response.xpath("//meta[@property='product:price:amount']/@content")[0].extract()

        object = yield {
            'productLinkId': self.link_dict[response.request.url],
            'price': float(best_price.replace(',', '.')),
            'timestamp': datetime.datetime.now()
        }
        url2 = 'http://localhost:8095/scrap'
        response2 = requests.post(url2, data=object)