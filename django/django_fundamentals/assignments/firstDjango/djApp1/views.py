from django.http import HttpResponse

def register(request):
    return HttpResponse("placeholder for users to create a new user record.")

def login_view(request):
    return HttpResponse("placeholder for users to log in.")

def list_users(request):
    return HttpResponse("placeholder to display all the list of users later.")
