from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('test/',views.test,name = 'test'),
    path('yourlist/', views.ListListView.as_view(), name="yourlist"),
    path('yourlist/<int:pk>/', views.ListDetailView.as_view(), name = 'list_detail')
]
