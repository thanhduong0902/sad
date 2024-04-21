from django.db import models
from book.models import Book

class CartItem(models.Model):
    product_id = models.CharField(max_length=255)  # Chuỗi tương ứng với book_id
    quantity = models.PositiveIntegerField(default=1)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)  # Khóa ngoại đến mô hình Book

    def __str__(self):
        return f"{self.quantity} x {self.book.title}"
