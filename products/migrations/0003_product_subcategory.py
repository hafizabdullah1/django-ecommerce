# Generated by Django 5.0.6 on 2024-07-08 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_categories_categorie'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.CharField(default='t-shirts', max_length=100),
            preserve_default=False,
        ),
    ]
