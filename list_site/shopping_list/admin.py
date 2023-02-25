from django.contrib import admin
from .models import List, Item

# Register your models here.
class ListAdmin(admin.ModelAdmin):
    list_display = ('title','date_created')

admin.site.register(List)
admin.site.register(Item)