import scrapy
import datetime
import json
import requests

class KomputronikSpider(scrapy.Spider):

    name = 'komputronik'
    allowed_domains = ['komputronik.pl']

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

        object = yield {
            'productLinkId': self.link_dict[response.request.url],
            'price': float(result.replace(" ", "")),
            'timestamp': datetime.datetime.now()
        }
        url2 = 'http://localhost:8095/scrap'
        response2 = requests.post(url2, data=object)



