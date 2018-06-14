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
        page = response.url.split("/")[-1]
        page = page.split(",")[0]
        filename = 'empik-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

