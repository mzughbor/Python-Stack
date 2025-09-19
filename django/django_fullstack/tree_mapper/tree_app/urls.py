from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.index, name="home"),
    path('<int:id>', views.view_tree, name="view_tree"),
    path('new', views.new, name="new"), # GET route
    path('create_tree', views.create_tree, name="create_tree"), # POST route
    path('delete_tree/<int:id>', views.delete_tree, name="delete_tree"),
    path('update_tree/<int:id>', views.update_tree, name="update_tree"),
    path('add_visit/<int:id>', views.add_visit, name="add_visit")
]
