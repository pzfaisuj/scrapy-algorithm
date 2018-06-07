# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector

class CeneoSpider(scrapy.Spider):
    name = 'ceneo'
    allowed_domains = ['ceneo.pl']
    start_urls = [
        'https://www.ceneo.pl/47629930' ]

    def parse(self, response):
        #response.css('tr').xpath('@data-price').extract()
        
        offers = response.css(".product-offer")
        item_name = response.xpath('//*[@id="body"]/div[2]/div/div/div[1]/article/table/tr[2]/td/h1/text()').extract()
        item_image = response.xpath('//*[@class="js_gallery-anchor js_image-preview"]/img/@src').extract()
        
        for offer in offers:
            yield {
                    'name': item_name,
                    'shop_name': offer.xpath('@data-shopurl').extract(),
					'price': offer.xpath('@data-price').extract(),
					'imageURL': item_image ,
                    'productUrl': offer.xpath('./td[1]/a/@href').extract(),
					'description': offer.css('.short-name__txt ::text').extract() 
                  }