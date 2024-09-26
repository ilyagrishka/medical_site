from django.contrib import admin

from med_service.models import Categories, Product


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "price", "discount"]
    list_editable = ["discount"]
    search_fields = ["name"]
    list_filter = ["discount", "category"]
