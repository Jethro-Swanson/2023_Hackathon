# Generated by Django 4.1.5 on 2023-02-25 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_list', '0005_post_delete_shoplist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='id',
        ),
        migrations.AddField(
            model_name='list',
            name='list_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
