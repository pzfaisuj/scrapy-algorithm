# -*- coding: utf-8 -*-
import scrapy

class SkapiecRowerySpider(scrapy.Spider):

    name = "rowery"
    
    def start_requests(self):
        url = 'https://www.skapiec.pl/cat/2215/page/1'
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = url + 'tag/' + tag
        yield scrapy.Request(url, self.parse)

		#name = 'skapiec_rowery'
    #allowed_domains = ['skapiec.pl']
    #start_urls = ['https://www.skapiec.pl/cat/2215/page/1',
    #'https://www.skapiec.pl/cat/2215/page/2',
    #'https://www.skapiec.pl/cat/2215/page/3']

#    rules = (
#        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
#    )

    def parse(self, response):
        for bikes in response.css('a.box'):
            yield {
                'name': bikes.css('h2.title::text').extract_first()
            }

        #next_page = response.css('li.next a::attr(href)').extract_first()
        #if next_page is not None:
         #   yield response.follow(next_page, self.parse)
