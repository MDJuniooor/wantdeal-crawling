from django.db import models

class HotDeal(models.Model):
    site_post_id = models.IntegerField(unique=True, blank=True, null=True)
    site = models.CharField('사이트',max_length=255, blank=True, null=True)
    title = models.CharField('제목',max_length=255, blank=True, null=True)
    category = models.CharField('카테고리',max_length=255, blank=True, null=True)
    location = models.CharField('지역',max_length=255, blank=True, null=True)
    is_closed = models.CharField('종료여부',max_length=255, blank=True, null=True)
    url = models.CharField('URL',max_length=255, blank=True, null=True)
    price = models.DecimalField('가격', max_digits=15, decimal_places=2, blank=True, null=True)
    photo = models.ImageField('이미지', blank=True, null=True)
    
    def __str__(self):
        return self.title
