from django.contrib import admin

from product.models.models import Product, ProductIntensity, ProductType, ProductStock, ProductImage

admin.site.register(Product)

admin.site.register(ProductIntensity)

admin.site.register(ProductType)

admin.site.register(ProductStock)

admin.site.register(ProductImage)
