from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('post_message', views.post_message),
    path('post_comment/<int:id>', views.post_comment),
    path('delete_message/<int:id>', views.delete_message)
]
