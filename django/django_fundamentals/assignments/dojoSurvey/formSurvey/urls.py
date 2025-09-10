from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('users', views.create_user, name="create_user"),
    path('result', views.result, name="result"),
    path('success', views.success_message, name="success")
]
