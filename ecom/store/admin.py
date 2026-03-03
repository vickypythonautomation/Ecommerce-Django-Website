from django.contrib import admin
from .models import Customer, Category, Order, Product
from django.utils.html import format_html

admin.site.register(Customer)
admin.site.register(Order)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'is_sale', 'sale_price', 'image_tag')
    list_filter = ('category', 'is_sale')
    search_fields = ('name', 'description')

    def image_tag(self, obj):
        if obj.image:
            return format_html('<a href="{}" target="_blank"><img src="{}" height="50" /></a>', obj.get_absolute_url(), obj.image.url)
        return ""
    image_tag.short_description = 'Image'

    def view_on_site(self, obj):
        return obj.get_absolute_url()

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
