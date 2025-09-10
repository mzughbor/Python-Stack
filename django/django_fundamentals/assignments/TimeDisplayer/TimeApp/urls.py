from django.urls import path, include
from . import views

urlpatterns = [
    # both firing same method
	path('', views.time_display, name='root_time_display'), 
	path('time_display/', views.time_display, name='time_display'),
]
