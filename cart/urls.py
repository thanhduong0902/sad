from django.urls import path
from . import views

urlpatterns = [
    path('add/<str:book_id>/', views.cart_add, name='cart_add'),
    path('view/',views.view_cart,name ='cart_view' )
]
