# Generated by Django 5.1 on 2024-08-18 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_alter_category_options_item'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Item',
        ),
    ]
