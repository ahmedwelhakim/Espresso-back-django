# Generated by Django 4.1.4 on 2023-01-05 13:03

import common.validators.file_size
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import functools
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.UUID("7a4a0bee-98a7-4e96-b422-5c60f26ec00d"),
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("name", models.TextField()),
                ("price", models.FloatField()),
                ("discount_price", models.FloatField()),
                ("description", models.TextField()),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ProductIntensity",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.UUID("63b5a9a4-a28b-4016-898a-1732994bc0bc"),
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("product_intensity", models.TextField()),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ProductType",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.UUID("1e471d12-9e4a-4dbf-9116-f6df6cbc19fc"),
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("product_type", models.TextField()),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ProductStock",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("quantities", models.IntegerField()),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="stock_product",
                        to="product.product",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ProductImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "image",
                    models.FileField(
                        upload_to="product/",
                        validators=[
                            functools.partial(
                                common.validators.file_size.validate_file_size,
                                *(),
                                **{"file_size": 10}
                            ),
                            django.core.validators.FileExtensionValidator(
                                [
                                    "jpg",
                                    "jpeg",
                                    "pdf",
                                    "txt",
                                    "png",
                                    "svg",
                                    "mpeg",
                                    "gif",
                                    "webm",
                                    "MOV",
                                    "mkv",
                                    "HEIC",
                                    "JPG",
                                    "PNG",
                                    "JPEG",
                                    "GIF",
                                    "SVG",
                                ],
                                "allowed format is :  'jpg', 'png', 'jpeg',  'gif','svg'... ",
                            ),
                        ],
                        verbose_name="Product Image",
                    ),
                ),
                ("is_main", models.BooleanField()),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="image_product",
                        to="product.product",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="product",
            name="product_intensity",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="product.productintensity",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="product_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="product.producttype"
            ),
        ),
    ]