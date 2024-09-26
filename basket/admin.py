from django.contrib import admin

from basket.models import Basket


# admin.site.register(Basket)
@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ["user", "product", "quantity", "created_timestamp"]
    list_filter = ["created_timestamp","user", "product"]
