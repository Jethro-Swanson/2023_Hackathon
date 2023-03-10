# Generated by Django 4.1.5 on 2023-02-25 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_list', '0003_shoplist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='list',
        ),
        migrations.AlterField(
            model_name='item',
            name='itemName',
            field=models.CharField(default='Def_Name', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='priority',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='list',
            name='title',
            field=models.CharField(default='Def_Title', max_length=100),
            preserve_default=False,
        ),
    ]
