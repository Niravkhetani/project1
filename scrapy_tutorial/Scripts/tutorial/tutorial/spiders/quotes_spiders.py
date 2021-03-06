import scrapy



class QuotesSpider(scrapy.Spider):
    name            = "quotes"

    # def start_requests(self):
    #     urls        = [
    #         'http://quotes.toscrape.com/page/1',
    #         'http://quotes.toscrape.com/page/2',
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url,callback=self.parse)
    start_urls          = [
            'http://quotes.toscrape.com/page/1',
            'http://quotes.toscrape.com/page/2',
    ]

    def parse(self,response):
        print("In parse")
        page        = response.url.split("/")[-2]
        filename    = f'qut-{page}.html'
        with open(filename,'wb') as f:
            f.write(response.body)
        self.log(f'saved file {filename}')


# import scrapy


# class QuotesSpider(scrapy.Spider):
#     name = "quotes"

#     # def start_requests(self):
#         # urls = [
#         #     'http://quotes.toscrape.com/page/1/',
#         #     'http://quotes.toscrape.com/page/2/',
#         # ]
#         # for url in urls:
#         #     yield scrapy.Request(url=url, callback=self.parse)
#     start_urls = [
#             'http://quotes.toscrape.com/page/1/',
#             'http://quotes.toscrape.com/page/2/',
#     ]

#     def parse(self, response):
#         page = response.url.split("/")[-2]
#         print("page",page)
#         filename = f'quotes-{page}.html'
#         with open(filename, 'wb') as f:
#             f.write(response.body)
#         self.log(f'Saved file {filename}')
