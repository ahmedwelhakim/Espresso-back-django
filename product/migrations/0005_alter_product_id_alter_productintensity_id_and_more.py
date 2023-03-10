# Generated by Django 4.1.4 on 2023-01-05 14:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        (
            "product",
            "0004_rename_product_intensity_productintensity_intensity_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("5dd5c30c-4303-4631-904e-5f35c2630f65"),
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="productintensity",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("076608ad-777b-4c57-86d5-bf38e05fe736"),
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="producttype",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("f63731b6-9a65-499c-8741-49388e755fbd"),
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
