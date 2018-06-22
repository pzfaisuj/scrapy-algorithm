import scrapy
import datetime
import json

class XkomSpider(scrapy.Spider):



    name = 'komputronik'
    allowed_domains = ['komputronik.pl']

    with open('../../komputronik_links.json') as json_data:
        links = json.load(json_data)
        # print(links)
    link_dict = {}
    for data in links:
        link_dict[data['link']] = data['id']

    start_urls = link_dict.keys()

    # start_urls = []
    # for i in range(1, 16):
    #     start_urls.append('https://www.komputronik.pl/category/1596/smartfony.html?p=' + str(i))
    # # start_urls = ['https://www.komputronik.pl/category/1596/smartfony.html']

    cls = "product-entry2-wrap"

    def strip(self, string):

        if not string:
            return ""

        if type(string) is str:
            return " ".join(string.split())
        if type(string) is list:
            try:
                return " ".join(string[0].split())
            except IndexError:
                print("WTF ", string)

    def parse(self, response):

        price = response.css('html body.fgm-fixed ktr-site div#content-wrapper ktr-product div ktr-transclude div#p-inner.pgrid-container div#p-inner-right.col-xs-30.col-lg-8.pull-right div.row div.col-md-14.col-lg-30 section#p-inner-prices div.prices span.price span.proper')
        result = self.strip(response.css("span.proper:nth-child(1)")[0].select("text()").extract()[0])

        yield {
            'product_link_id': self.link_dict[response.request.url],
            'price': float(result.replace(" ", "")),
            'timestamp': datetime.datetime.now()
        }



