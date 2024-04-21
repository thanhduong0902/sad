import requests
from django.shortcuts import render

def home(request):
    # Gọi API từ ứng dụng Book
    response = requests.get('http://localhost:8000/book/all')
    books = response.json()

    return render(request, 'home.html', {'books': books})