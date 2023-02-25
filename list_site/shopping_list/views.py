from django.shortcuts import render
from .models import List, Item
from django.views import generic
from django.views.generic.edit import(
    CreateView,
    UpdateView,
    DeleteView,
)

# Create your views here.
def home(request):
    return render(request,'home.html')

def test(request):
    return render(request,'test.html')


class ListListView(generic.ListView):
    model = List
   # context_object_name = 'shopping_list'

class ListCreate(CreateView):
    model = List
    fields = ["title"]

    '''def get_context_data(self):
        context = super(ListCreate, self).get_context_data()
        context["title"] = "Add a new list"
        return context'''

class ItemCreate(CreateView):
    model = Item
    fields = [
        "itemName",
        "description",
        "priority",
    ]

class ListUpdate(UpdateView):
    model = List
    fields = '__all__'

class ItemUpdate(UpdateView):
    model = Item
    fields = '__all__'
