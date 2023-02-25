from django.db import models
from django.urls import reverse

# Create your models here.
class List(models.Model):
    title = models.CharField(max_length=100,null=True)
    date_created = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('list_detail', args=[str(self.id)])

    def get_pk(self):
        return str(self.id)

    def __str__(self):
        return self.title
    

class Item(models.Model):
    itemName = models.CharField(max_length=100,null=True)
    description = models.TextField()
    priority = models.CharField(max_length=100, null=True)
    date_modified = models.DateField(auto_now=True)
    list = models.ForeignKey('List',related_name='items',on_delete=models.CASCADE, null= True)

    class Meta:
        ordering = ['-date_modified']

    def __str__(self):
        return self.itemName

class ShopList(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("shop_detail", kwargs={"pk": self.pk})
    