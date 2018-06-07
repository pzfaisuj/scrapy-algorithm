import scrapy


class XkomSpider(scrapy.Spider):



    name = 'komputronik'
    allowed_domains = ['komputronik.pl']
    start_urls = []
    for i in range(1, 16):
        start_urls.append('https://www.komputronik.pl/category/1596/smartfony.html?p=' + str(i))
    # start_urls = ['https://www.komputronik.pl/category/1596/smartfony.html']
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


        product_list = response.css('.product-entry2')
        for product in product_list:

            try:
                pr_id = product.xpath('.//div[@class="pe2-codes"]/text()').extract()
            except IndexError:
                pr_id = "Not available"

            try:
                descr = product.xpath('.//div[@class="inline-features"]/span/text()').extract()[0]
            except IndexError:
                descr = str("Not available")


            yield {
                'name': self.strip(product.xpath('.//div[@class="pe2-head"]/a/text()').extract()[0].splitlines()[1]),
                'price': self.strip(product.xpath('.//div[@class="ps4-price"]/span/text()').extract()[0]),
                'imageURL': product.xpath('.//div[@class="pe2-head"]/a/@href').extract(),
                'productId': self.strip(pr_id),
                'productUrl': str(product.xpath('.//div[@class="pe2-img"]/a/img/@data-src').extract())[4:],
                'description': self.strip(descr)

            }



