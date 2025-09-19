from django.urls import path
from . import views
from tree_app import views as treesview

urlpatterns = [
    path('', views.index, name="home"),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('check-email/', views.check_email, name="check_email"),
]
