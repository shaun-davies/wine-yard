from django.contrib import admin
from .models import Product, Category, Country, ProductReview

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'country',
        'price',
        'size',
        'image',
    )

class ProductReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'user',
        'review',
        'user_name',
        'rating'
    )

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('friendly_name', 'name',)

class CountryAdmin(admin.ModelAdmin):
    list_display = ('friendly_name', 'name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
