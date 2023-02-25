from django.db import models
from django.urls import reverse

# Create your models here.
class List(models.Model):
    list_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    itemName = models.CharField(max_length=100)
    description = models.TextField()
    priority = models.CharField(max_length=100)
    date_modified = models.DateField(auto_now=True)
    #list = models.ForeignKey('List',related_name='items',on_delete=models.CASCADE, null= True)

    class Meta:
        ordering = ['-date_modified']

    def __str__(self):
        return self.itemName
        
    