import scrapy


class PagerSpider(scrapy.Spider):
    name = "pager"
    allowed_domains = ["example.com"]
    start_urls = ["https://example.com"]

    def parse(self, response):
        pass
