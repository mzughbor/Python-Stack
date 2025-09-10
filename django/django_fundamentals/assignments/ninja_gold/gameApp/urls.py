from django.urls import path
from . import views

urlpatterns = [
	path('', views.root, name="home"),
    path('process_money', views.process_money, name="process_money"),
    path('reset', views.reset, name='reset'),
]