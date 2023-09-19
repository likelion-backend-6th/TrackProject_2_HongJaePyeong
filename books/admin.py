from datetime import date

from django.contrib import admin
from django.shortcuts import get_object_or_404

from .models import Book, Rental


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publisher', 'stock']  # 목록에서 보여줄 필드
    search_fields = ['title', 'author', 'publisher']  # 검색 가능한 필드
    list_filter = ['author', 'publisher']  # 필터링 가능한 필드


def return_book(modeladmin, request, queryset):
    queryset.update(return_date=date.today())
    # 도서 재고 증가
    for rental in queryset:
        book = rental.book
        book.stock += 1
        book.save()


@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ['user', 'book', 'rental_date', 'return_date']  # 목록에서 보여줄 필드
    search_fields = ['user__username', 'book__title']  # 검색 가능한 필드, ForeignKey 필드 검색을 위해 '__' 사용
    list_filter = ['rental_date', 'return_date']  # 필터링 가능한 필드
    actions = [return_book]

