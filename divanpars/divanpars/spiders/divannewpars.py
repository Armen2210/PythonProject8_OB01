import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://www.divan.ru/sankt-peterburg/"]
    start_urls = ["https://www.divan.ru/sankt-peterburg/category/svet"]

    def parse(self, response):
        lamps = response.css('div.ProductCard_container__HLDPH')
        for lamp in lamps:
            yield {
                'name': lamp.css('div.ProductCard_info__c9Z_4 span::text').get(),
                'price': lamp.css('div.ProductCard_wrapperPrice__91mtE span::text').get(),
                'url': lamp.css('a').attrib['href']
            }


