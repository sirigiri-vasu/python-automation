from typing import Any

import scrapy
from scrapy.http import Response

from ..items import QuoterItem

class QuotesScrapy(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com/'
    ]

    def parse(self, response: Response, **kwargs: Any) -> Any:
        items = QuoterItem()
        all_div_quotes = response.css('div.quote')

        for div_quote in all_div_quotes:
            title = div_quote.css('span.text::text').extract()
            author = div_quote.css('.author::text').extract()
            tags = div_quote.css('.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tags'] = tags
            yield items
