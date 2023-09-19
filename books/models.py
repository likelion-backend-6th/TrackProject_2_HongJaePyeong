from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    stock = models.IntegerField()  # 재고
    summary = models.TextField()

    def __str__(self):
        return self.title


class Rental(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)  # 대출 중인 도서가 삭제되면 null 처리
    rental_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)  # 아직 반납되지 않았다면 null

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    submitted_date = models.DateField(auto_now_add=True)
    rating = models.IntegerField(MinValueValidator(1), MaxValueValidator(5))
    content = models.TextField()

    def __str(self):
        return f"{self.book.title} - {self.rating}"
