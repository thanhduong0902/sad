from django.urls import path
from . import views

urlpatterns = [
    # path('', views.ApiOverview, name='mobile'),
    path('create/', views.add_items, name='add-mobile'),
    path('all/', views.view_items, name='view-mobile'),
    path('update/<str:pk>/', views.update_items, name='update-mobile'),
    path('delete/<str:pk>/', views.delete_items, name='delete-mobile'),
    path('search/',views.search_items,name='search-mobile')
]