from django.urls import path

from books import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('<int:book_id>/', views.book_detail, name='book_detail'),
    path('<int:book_id>/rent/', views.rent_book, name='rent_book'),
    path('<int:book_id>/review/', views.book_review, name='book_review'),
    path('my_rentals/', views.user_rentals, name='user_rentals'),
]
