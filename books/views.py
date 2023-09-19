from datetime import date

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from .models import Book, Rental, Review
from .forms import ReviewForm


def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})


@login_required
def book_detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    reviews = Review.objects.filter(pk=book_id)
    return render(request, 'books/book_detail.html', {'book': book, 'reviews': reviews})


@login_required
def rent_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    if book.stock > 0:
        Rental.objects.create(user=request.user, book=book)
        book.stock -= 1
        book.save()
    return redirect('book_detail', book_id=book_id)


@login_required
def user_rentals(request):
    rentals = Rental.objects.filter(user=request.user)
    return render(request, 'books/user_rentals.html', {'rentals': rentals})


@login_required
@require_POST
def book_review(request, book_id):
    book = Book.objects.get(pk=book_id)
    form = ReviewForm(request.POST)
    if form.is_valid():
        r = form.save(commit=False)
        data = form.cleaned_data
        r.book = book
        r.user = request.user
        r.rating = data['rating']
        r.content = data['content']
        r.save()
    return redirect('books/book_detail.html', book_id=book_id)
