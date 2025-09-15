from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('success', views.success, name="success"),
    path('check-email/', views.check_email, name="check_email"),
]
