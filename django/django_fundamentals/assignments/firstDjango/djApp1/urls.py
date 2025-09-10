from django.urls import path
from . import views

from blogs.views import index as blogs_index

urlpatterns = [
    
    # Root uses the same method as /blogs imported from blogs views
    path('', blogs_index, name='root_as_blogs'),

    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path('users/new', views.register, name='users_new'), # /users/new ---> same as /register
    path('users', views.list_users, name='users_list'),  # /users
]
