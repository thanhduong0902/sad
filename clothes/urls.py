from django.urls import path
from . import views

urlpatterns = [
    # path('', views.ApiOverview, name='clothes'),
    path('create/', views.add_items, name='add-clothes'),
    path('all/', views.view_items, name='view-clothes'),
    path('update/<str:pk>/', views.update_items, name='update-clothes'),
    path('clothes/<str:pk>/delete/', views.delete_items, name='delete-clothes'),
    path('search/',views.search_items,name='search')
]