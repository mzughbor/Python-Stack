from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('shows', views.index),
    path('shows/new', views.new),
    path('shows/create', views.create), # POST route
    path('shows/<int:id>', views.show),
    path('shows/<int:id>/edit', views.edit),
    path('shows/<int:id>/update', views.update), # POST route
    path('shows/<int:id>/destroy', views.destroy), # POST route


    path('shows/ajax/create/', views.ajax_create_show, name='ajax_create_show'),
    path('shows/ajax/update/<int:id>/', views.ajax_update_show, name='ajax_update_show'),

]
