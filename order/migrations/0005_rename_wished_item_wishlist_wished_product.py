# Generated by Django 4.1 on 2022-09-16 01:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_wishlist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wishlist',
            old_name='wished_item',
            new_name='wished_product',
        ),
    ]
