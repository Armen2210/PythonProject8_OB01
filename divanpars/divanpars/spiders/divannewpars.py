import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://www.divan.ru/sankt-peterburg/"]
    start_urls = ["https://www.divan.ru/sankt-peterburg/category/svet?sort=1"]

    def parse(self, response):
        divans = response.xpath('div.Ud0K')
        for divan in divans:
            yield {
                # Ссылки и теги получаем с помощью консоли на сайте
                # Создаём словарик названий, используем поиск по диву, а внутри дива — по тегу span
                'name': divan.css('div.lsooF span::text').get(),
                # Создаём словарик цен, используем поиск по диву, а внутри дива — по тегу span
                'price': divan.css('div.pY3d2 span::text').get(),
                # Создаём словарик ссылок, используем поиск по тегу "a", а внутри тега — по атрибуту
                # Атрибуты — это настройки тегов
                'url': divan.css('a').attrib['href']
            }