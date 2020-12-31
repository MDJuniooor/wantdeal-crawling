import scrapy
from furl import furl
import functools
from hotdealscraper.items import HotDealItem

class BbomBbuSpider(scrapy.Spider):
    name = "bbombbu"

    category = {
        "ppomppu" : "전체",
        "ppomppu4" : "해외",
        "pmarket" : "쇼핑/보험"
    }

    def start_requests(self):
        urls = [
            'http://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu', # 뽐뿌게시판
            'http://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu4', # 뽐뿌해외
            'http://www.ppomppu.co.kr/zboard/zboard.php?id=pmarket', # 쇼핑/보험뽐뿌
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        rows = response.css('.list0 tr a, .list1 tr a').xpath('@href').extract()
     
        for row in rows: 
            url = 'http://www.ppomppu.co.kr/zboard/' + row
            qp = furl(url) 
            info = {
                "url" : url,
                "category" : self.category[qp.args['id']],
                "site_post_id" : qp.args['no']
            }
            callback = functools.partial(self.parse_item, info)
            yield scrapy.Request(url=url, callback=callback)

    def parse_item(self, info, response):
        i = HotDealItem()
        i['title'] = response.css('.view_title2 *::text').extract_first()
        i['site'] = '뽐뿌'
        i['category'] = info['category']
        i['url'] = info['url']
        i['site_post_id'] = info['site_post_id']

        # i['phachase_site'] = response.css('.wordfix a *::text').extract_first()
        image_source = response.css('.board-contents img').xpath('@src').extract()

        if image_source:
            i['image_urls'] = 'http:' + image_source
        return i