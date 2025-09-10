from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blogs_index'),
    path('new/', views.new, name='blogs_new'),
    path('create/', views.create, name='blogs_create'),
    path('<int:number>/', views.show, name='blogs_show'),
    path('<int:number>/edit/', views.edit, name='blogs_edit'),
    path('<int:number>/delete/', views.destroy, name='blogs_delete'),
    path('blogs/json', views.jsonResponse)
]
