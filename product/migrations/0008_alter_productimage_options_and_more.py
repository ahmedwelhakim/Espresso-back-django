# Generated by Django 4.1.4 on 2023-01-09 09:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0007_alter_product_id_alter_productintensity_id_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="productimage",
            options={"verbose_name_plural": "Product Images"},
        ),
        migrations.AlterModelOptions(
            name="productintensity",
            options={"verbose_name_plural": "Product Intensities"},
        ),
        migrations.AlterModelOptions(
            name="productstock",
            options={"verbose_name_plural": "Product Stocks"},
        ),
        migrations.AlterModelOptions(
            name="producttype",
            options={"verbose_name_plural": "Product Types"},
        ),
        migrations.AlterField(
            model_name="product",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("6a0fd521-3504-4321-9dfc-6b0e6e3de0dd"),
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
                default=uuid.UUID("a75dee50-65c6-44e5-8704-f30bed6bee5c"),
                editable=False,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="producttype",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("63d7df61-c1c4-47e9-8687-8d7cbf4349a4"),
                editable=False,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
