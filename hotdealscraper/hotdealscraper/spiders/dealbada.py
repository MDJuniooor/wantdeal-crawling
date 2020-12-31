import scrapy
from furl import furl
import functools
from hotdealscraper.items import HotDealItem

class DealbadaSpider(scrapy.Spider):
    name = "dealbada"

    category = {
        "deal_domestic" : "국내딜",
        "ppomppu4" : "해외",
        "pmarket" : "쇼핑/보험"
    }

    def start_requests(self):
        urls = [
            'http://www.dealbada.com/bbs/board.php?bo_table=deal_domestic', #국내핫딜
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        rows = response.css('.td_subject a').xpath('@href').extract()
     
        for row in rows: 
            url = row
            qp = furl(url) 
            info = {
                "url" : url,
                "site_post_id" : qp.args['wr_id']
            }
            callback = functools.partial(self.parse_item, info)
            yield scrapy.Request(url=url, callback=callback)

    def parse_item(self, info, response):
        i = HotDealItem()
        i['title'] = response.css('#bo_v_info div > span *::text').extract_first()
        i['site'] = '딜바다'
        i['category'] = response.css('#bo_v_info div > span *::text').extract()[1]
        i['url'] = info['url']
        i['site_post_id'] = info['site_post_id']

        # i['phachase_site'] = response.css('.wordfix a *::text').extract_first()
        image_source = response.css('#bo_v_con img').xpath("@src").extract()

        if image_source:
            i['image_urls'] = image_source
        if i['category'] == ['공지']:
            return None
        return i