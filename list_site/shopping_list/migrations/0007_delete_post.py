# Generated by Django 4.1.5 on 2023-02-25 22:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_list', '0006_remove_list_id_list_list_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]