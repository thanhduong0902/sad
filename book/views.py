from rest_framework.decorators import api_view
from bson import ObjectId
from rest_framework.response import Response
from .models import Book
from .serlializers import BookSerializer
from rest_framework import status
from db_connection import db
from rest_framework import serializers
import re
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
collection = db['book']

@csrf_exempt
def add_items(request):
    if request.method == 'POST':
        book_data = JSONParser().parse(request)
        book_serializer = BookSerializer(data=book_data)
        if book_serializer.is_valid():
            collection.insert_one(book_serializer.data)  # This will automatically handle the saving of the object with an auto-generated id
            return JsonResponse(book_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Handle cases where request method is not POST
    return JsonResponse({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
@api_view(['GET'])
def view_items(request):
    query_params = request.query_params
    if query_params:
        # Tạo biểu thức chính quy để tìm kiếm một phần của giá trị
        regex_pattern = re.compile(f"{query_params.get('search')}", re.IGNORECASE)
        # Tìm kiếm các mục trong 'name' hoặc 'brand' chứa từ khóa nhập vào
        query = {
            "$or": [
                {"title": {"$regex": regex_pattern}},
                {"author": {"$regex": regex_pattern}}
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


@api_view(['GET'])
def book_detail(request, pk):
    try:
        query = {"_id": ObjectId(pk)}
        result = collection.find_one(query)
        
        if result:
            # Chuyển đổi ObjectId thành str trước khi trả về
            result['_id'] = str(result['_id'])
            return Response(result)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



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
def search_item(request):
    query_params = request.query_params
    if query_params:
        # Tạo biểu thức chính quy để tìm kiếm một phần của giá trị
        regex_pattern = re.compile(f"{query_params.get('keyword')}", re.IGNORECASE)
        # Tìm kiếm các mục trong 'name' hoặc 'brand' chứa từ khóa nhập vào
        query = {
            "$or": [
                {"title": {"$regex": regex_pattern}},
                {"author": {"$regex": regex_pattern}}
            ]
        }
        
        books = collection.find(query)
    else:
        books = collection.find()
 
    books_list = list(books)
    if books_list:
        for book in books_list:
            book['_id'] = str(book['_id'])
        return Response(books_list)
        # return Response({'success':True})
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

