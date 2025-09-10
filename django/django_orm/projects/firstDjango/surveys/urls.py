from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='surveys_index'),  # /surveys
    path('new', views.new, name='surveys_new'),   # /surveys/new
]
