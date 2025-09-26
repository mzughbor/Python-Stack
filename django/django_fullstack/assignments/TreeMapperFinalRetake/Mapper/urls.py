from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('dashboard', views.success, name="dashboard"),
    path('check-email/', views.check_email, name="check_email"),
    path('trees/new', views.new_tree_form, name="new_tree_form"),
    path('trees/new_tree', views.post_tree_req, name="post_tree_req"),
    path('trees/<int:id>/delete', views.delete_tree, name="delete_tree"),
    path('trees/edit/<int:id>', views.edit_tree, name="edit_tree_form"),
    path('trees/<int:id>', views.view_tree, name="view_tree"),
    path('trees/visit/<int:id>', views.toggle_visit, name="toggle_visit")
]
