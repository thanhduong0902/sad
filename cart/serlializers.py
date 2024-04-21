# serializers.py
from rest_framework import serializers
from .models import CartItem
from book.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'des', 'price']

class CartItemSerializer(serializers.ModelSerializer):
    book = BookSerializer()  # Sử dụng BookSerializer để bao gồm thông tin chi tiết của sách

    class Meta:
        model = CartItem
        fields = ['id', 'book', 'quantity']
