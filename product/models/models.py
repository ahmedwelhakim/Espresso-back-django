import functools
import uuid

from django.core.validators import FileExtensionValidator

from common.models import BaseModel
from django.db import models

from common.validators.file_size import validate_file_size
from common.validators import image_validators
from espresso import settings


class Product(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), unique=True, editable=False)
    name = models.TextField()
    price = models.FloatField()
    discount_price = models.FloatField()
    description = models.TextField()
    product_type = models.ForeignKey('ProductType', related_name='product_type', on_delete=models.CASCADE, db_index=True)
    product_intensity = models.ForeignKey('ProductIntensity', related_name='product_intensity', on_delete=models.CASCADE, db_index=True)

    def __str__(self):
        return f'{self.name}: {self.price}LE'


class ProductType(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    type = models.TextField()

    def __str__(self):
        return self.product_type


class ProductIntensity(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    intensity = models.TextField()

    def __str__(self):
        return self.intensity


class ProductImage(BaseModel):
    image = models.FileField(upload_to="product/", verbose_name="Product Image",
                             validators=[
                                 functools.partial(validate_file_size, file_size=settings.IMAGE_SIZE),
                                 FileExtensionValidator(image_validators.allowed_extensions,
                                                        image_validators.extension_error_message)
                             ])
    is_main = models.BooleanField()
    product = models.ForeignKey('Product', related_name='image_product', on_delete=models.CASCADE, db_index=True)


class ProductStock(BaseModel):
    product = models.OneToOneField('Product', related_name='stock_product', on_delete=models.CASCADE, db_index=True)
    quantities = models.IntegerField()

    def __str__(self):
        return self.quantities
