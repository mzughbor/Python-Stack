from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('<int:id>', views.view_book, name="view_book"),
    path('post_book', views.post_book),
    path('delete_book/<int:id>', views.delete_book, name="delete_book"),
    path('update_book/<int:id>', views.update_book, name="update_book"),
    path('add_fav/<int:id>', views.add_fav, name="add_fav"),
    path('delete_fav/<int:id>', views.delete_fav, name="delete_fav")
]
