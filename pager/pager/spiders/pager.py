import scrapy

from ..items import PagerItem


class ExampleSpider(scrapy.Spider):
    name = "pager"
    start_urls = ["https://quotes.toscrape.com/page/1/"]

    def parse(self, response):
        items = PagerItem()

        divs = response.css("div.quote")
        for div in divs:
            title = div.css("span.text::text").extract()
            author = div.css(".author::text").extract()
            tags = div.css(".tag::text").extract()

            items['title'] = title
            items['author'] = author
            items['tags'] = tags

            yield items

        next_page = response.css("li.next a::attr(href)").get()
        print(next_page)
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
