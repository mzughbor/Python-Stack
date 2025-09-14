from django.urls import path
from . import views
from wall_app import views as wallview

urlpatterns = [
    path('', views.index, name="home"),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('check-email/', views.check_email, name="check_email"),
]
