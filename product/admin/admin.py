from django.contrib import admin
# from django.db.models import Prefetch, Q, F
# from django.db.models.query import RawQuerySet, QuerySet
# from django.db.models.sql import Query
# from django.db import connections
#
# from django.utils.safestring import mark_safe

from product.models import Product, ProductImage

# admin.site.register(ProductIntensity)
#
# admin.site.register(ProductType)
#
# admin.site.register(ProductStock)
# admin.site.register(ProductImage)


class ProductImageInline(admin.TabularInline):
    model = ProductImage


# class ProductStockInline(admin.TabularInline):
#     model = ProductStock


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]

    # list_display = ["name", "product_type","image_view"]
    #
    # def has_add_permission(self, request):
    #     return True
    #
    # def has_change_permission(self, request, obj=None):
    #     return True
    #
    # def has_module_permission(self, request):
    #     return True
    #
    # @admin.display(description='Image')
    # def image_view(self, instance):
    #     try:
    #         return mark_safe(
    #             f'<img src = "{instance.productimage_set.all()[0].image.url}" width = "80"/>')
    #
    #     except:
    #         return mark_safe(
    #             f'<p>image not found</p>')
    #
    # def get_queryset(self, request):
    #     print('ss')
    #     qs = Product.objects.prefetch_related(
    #         Prefetch('productimage_set', queryset=ProductImage.objects.filter(is_main=True))).order_by('-created_at')
    #     return qs
