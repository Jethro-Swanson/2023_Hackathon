# Generated by Django 4.1.5 on 2023-02-25 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_list', '0002_remove_list_items_item_list_alter_item_itemname_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
    ]
