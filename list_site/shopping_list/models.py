from django.db import models

# Create your models here.
class List(models.Model):
    title = models.CharField(max_length=100)
    items = models.TextField(null = True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    


class Item(models.Model):
    itemName = models.CharField(max_length=100)
    description = models.TextField()
    priority = models.CharField(max_length=100)
    date_modified = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-date_modified']

    def __str__(self):
        return self.itemName

    