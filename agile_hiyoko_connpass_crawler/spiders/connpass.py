import scrapy


class ConnpassSpider(scrapy.Spider):
    name = 'connpass'
    allowed_domains = ['connpass.com']
    start_urls = ['http://connpass.com/']

    def parse(self, response):
        pass
