from django.http import HttpResponse
from django.shortcuts import render


from .models import Movie

def register(request):
    return HttpResponse("placeholder for users to create a new user record.")

def login_view(request):
    return HttpResponse("placeholder for users to log in.")

def list_users(request):
    return HttpResponse("placeholder to display all the list of users later.")


# show all of the data from a table
def index(request):
    context = {
        "all_the_movies": Movie.objects.all()
    }
    return render(request, "index.html", context)