# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector

class VobisSpider(scrapy.Spider):
    name = 'vobis'
    allowed_domains = ['vobis.pl']
    start_urls = ['https://vobis.pl/mobile/smartfony']

    def parse(self, response):
        results = response.css('.m-offerBox_name')
        print len(results)
        for result in results:
            str = 'https://vobis.pl'
            str2 = result.xpath('./div/h2/a/@href').extract()
            str3 = ''.join(str2)
            str += str3
            yield {
                    'name': result.xpath('./div/h2/a/@data-offer-name').extract()[0],
					'price': result.xpath('./div/h2/a/@data-offer-price').extract()[0],
					# 'imageURL': result.xpath('./div/div/h2/a/img/@src').extract()[0],
					'productId': result.xpath('./div/h2/a/@data-offer-id').extract()[0],
                    'productUrl': str
					# 'description': result.xpath('./div/div/h2/a/@').extract()[0]
                  }
