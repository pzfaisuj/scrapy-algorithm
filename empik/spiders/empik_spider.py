# -*- coding: utf-8 -*-
import scrapy


class EmpikSpider(scrapy.Spider):
    name = "empik"

    def start_requests(self):
        urls = [
            "http://www.empik.com/ksiazki,31,s?hideUnavailable=true",
            "http://www.empik.com/film,33,s",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for empik_book in response.css("div.search-list-item"):
            yield {
                'author': empik_book.css("a.smartAuthor::text").extract_first().strip(),
                'title': empik_book.css("a.seoTitle strong::text").extract_first().strip(),
                'category': empik_book.css("span.productMainInfoSuffix::text").extract()[0].strip(),
                'medium': empik_book.css("span.productMainInfoSuffix::text").extract()[1].strip(),
                'price': empik_book.css("div.price::text").extract_first().encode('ascii', 'replace').strip()[:-3]
            }
