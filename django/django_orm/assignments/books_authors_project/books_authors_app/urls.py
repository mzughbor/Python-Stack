from django.urls import path
from . import views

urlpatterns = [
	path('', views.root, name="home"),
	path('add-book', views.add_new_book),
	path('book/<int:id>/', views.book_details, name="book_details"),
	path('book/<int:id>/add_author', views.add_author),
	path('author', views.author, name="authors"),
	path('add-author', views.add_new_author),
	path('author/<int:id>/', views.author_details, name="author_details"),
	path('author/<int:id>/add_book', views.add_book)
]