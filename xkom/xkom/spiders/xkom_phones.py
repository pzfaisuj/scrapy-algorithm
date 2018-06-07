# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector

class XkomSpider(scrapy.Spider):
    name = 'xkom'
    allowed_domains = ['x-kom.pl']
    start_urls = ['https://www.x-kom.pl/g-4/c/1590-smartfony-i-telefony.html']

    def parse(self, response):
#phones = []
#results = response.selector.xpath('//div[@class="product-item product-impression"]').extract()
#for result in results:
#    item = SklepyItem()
#    item['name'] = result.xpath('//div[@class="description-wrapper"]/text').extract()
#    item['price'] = response.xpath('//div[@data-product-price]').extract()
#    phones.append(item)
#return phones
        results = response.css('.product-item')
        for result in results:
            str = 'https://www.x-kom.pl'
            str2 = result.xpath('./div/a/@href').extract()
            str3 = ''.join(str2)
            str+=str3
            yield {
                    'name': result.xpath('./@data-product-name').extract()[0],
					'price': result.xpath('./@data-product-price').extract()[0],
					'imageURL': result.xpath('./a/img/@src').extract()[0],
					'productId': result.xpath('./@data-product-id').extract()[0],
                    'productUrl': str,
					'description': result.xpath('./div/div/ul/@title').extract()[0]
                  }