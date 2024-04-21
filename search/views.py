from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests

@api_view(['GET'])
def search_items(request):
    keyword = request.query_params.get('keyword', '')
    
    # Gửi yêu cầu tìm kiếm đến các dịch vụ và thu thập kết quả
    mobile_results = requests.get('http://localhost:8000/mobile/search/?keyword={keyword}')
    clothes_results = requests.get('http://localhost:8000/clothes/search/?keyword={keyword}')
    book_results = requests.get('http://localhost:8000/book/search/?keyword={keyword}')
    
    all_results = []
    all_results.extend(mobile_results)
    all_results.extend(clothes_results)
    all_results.extend(book_results)
    
    return Response(all_results)
