from django.http import JsonResponse
from .models import CartItem
from book.models import Book
from db_connection import db
from rest_framework.decorators import api_view
from rest_framework.response import Response
from bson.objectid import ObjectId
from .serlializers import CartItemSerializer
collection = db['book']
import re

@api_view(['POST'])
def cart_add(request, book_id):
    # Lấy thông tin về sách từ MongoDB
    book_info = collection.find_one({'_id': ObjectId(book_id)})
    
    if book_info:
        # Tạo hoặc lấy ra một đối tượng Book tương ứng
        book, _ = Book.objects.get_or_create(
            title=book_info['title'],
            author=book_info['author'],
            des=book_info['des'],
            price=book_info['price']
        )

        # Tạo một đối tượng CartItem và lưu vào cơ sở dữ liệu
        cart_item, created = CartItem.objects.get_or_create(
            book=book,
            defaults={'product_id': str(book_id), 'quantity': 1}  # Thiết lập mặc định cho trường product_id và quantity
        )

        # Tăng số lượng nếu cart_item đã tồn tại
        if not created:
            cart_item.quantity += 1
            cart_item.save()

        # Lấy thông tin về cart_item mới thêm vào giỏ hàng
        cart_data = {
            'id': cart_item.id,
            'book': cart_item.book.title,
            'quantity': cart_item.quantity
        }

        return JsonResponse({'success': cart_data})
    else:
        return JsonResponse({'error': 'Book not found'}, status=404)

@api_view(['GET'])
def view_cart(request):
    # Lấy tất cả các mục trong giỏ hàng
    cart_items = CartItem.objects.all()
    
    # Serialize dữ liệu
    serializer = CartItemSerializer(cart_items, many=True)
    
    # Trả về dữ liệu đã được serialize
    return Response(serializer.data)

