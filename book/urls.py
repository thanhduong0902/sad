from django.urls import path
from . import views

urlpatterns = [
    # path('', views.ApiOverview, name='book'),
    path('create/', views.add_items, name='add-book'),
    path('all/', views.view_items, name='view-book'),
    path('update/<str:pk>/', views.update_items, name='update-book'),
    path('delete/<str:pk>/', views.delete_items, name='delete-book'),
    path('detail/<str:pk>/',views.book_detail,name='detail-book'),
    path('search/',views.search_item,name='search-book')
]