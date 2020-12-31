import scrapy
from scrapy_djangoitem import DjangoItem
from apps.hotdeal.models import HotDeal

class HotDealItem(DjangoItem):
    django_model = HotDeal
    image_urls = scrapy.Field()
    images = scrapy.Field()
