# Generated by Django 4.1.4 on 2023-02-25 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_list', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='items',
        ),
        migrations.AddField(
            model_name='item',
            name='list',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='shopping_list.list'),
        ),
        migrations.AlterField(
            model_name='item',
            name='itemName',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='priority',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='list',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]