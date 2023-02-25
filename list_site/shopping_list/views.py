from django.shortcuts import render
from .models import List
from django.views import generic

# Create your views here.
def home(request):
    return render(request,'home.html')

def test(request):
    return render(request,'test.html')


class ListListView(generic.ListView):
    model = List
    context_object_name = 'shopping_list'

    