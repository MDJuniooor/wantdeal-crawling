from django.contrib import admin
from .models import HotDeal


class HotDealAdmin(admin.ModelAdmin):
    pass

admin.site.register(HotDeal, HotDealAdmin)