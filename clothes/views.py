from rest_framework.decorators import api_view
from bson import ObjectId
from rest_framework.response import Response
from .models import Clothes
from .serlializers import ClothesSerializer
from rest_framework import status
from db_connection import db
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import re
collection = db['clothes']
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def add_items(request):
    if request.method == 'POST':
        clothes_data = JSONParser().parse(request)
        clothes_serializer = ClothesSerializer(data=clothes_data)
        if clothes_serializer.is_valid():
            collection.insert_one(clothes_serializer.data)  # This will automatically handle the saving of the object with an auto-generated id
            return JsonResponse(clothes_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(clothes_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Handle cases where request method is not POST
    return JsonResponse({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
@api_view(['GET'])
def view_items(request):
    query_params = request.query_params
    if query_params:
        # Chuyển đổi từ khóa tìm kiếm và giá trị trong trường 'name' và 'brand' thành chữ thường hoặc chữ hoa
        keyword = query_params.get('keyword', '').lower()
        
        # Tạo biểu thức chính quy để tìm kiếm một phần của giá trị
        regex_pattern = re.compile(f"{re.escape(keyword)}", re.IGNORECASE)
        
        # Tìm kiếm các mục trong 'name' hoặc 'brand' chứa từ khóa nhập vào
        query = {
            "$or": [
                {"name": {"$regex": regex_pattern}},
                {"brand": {"$regex": regex_pattern}}
            ]
        }
        
        books = collection.find(query)
    else:
        books = collection.find()
 
    books_list = list(books)
    if books_list:
        # Chuyển đổi ObjectId thành str trước khi trả về kết quả
        for book in books_list:
            book['_id'] = str(book['_id'])
        return Response(books_list)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['PUT'])
def update_items(request, pk):
    query = {"_id": ObjectId(pk)}
    new_values = {"$set": request.data}
    result = collection.update_one(query, new_values)
 
    if result.modified_count > 0:
        return Response(request.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_items(request, pk):
    query = {"_id": ObjectId(pk)}
    result = collection.delete_one(query)
    if result.deleted_count > 0:
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def search_items(request):
    keyword = request.query_params.get('keyword', '').lower()
    regex_pattern = re.compile(f"{re.escape(keyword)}", re.IGNORECASE)
    
    query = {
        "$or": [
            {"name": {"$regex": regex_pattern}},
            {"brand": {"$regex": regex_pattern}}
        ]
    }
    
    clothes = collection.find(query)
    clothes_list = list(clothes)
    
    if clothes_list:
        for cloth in clothes_list:
            cloth['_id'] = str(cloth['_id'])
        return Response(clothes_list)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
