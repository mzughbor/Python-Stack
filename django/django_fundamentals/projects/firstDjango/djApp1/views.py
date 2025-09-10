from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

# Create your views here.
def root(request):
    return redirect("/blogs")

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect('/')

def show(request, number):
    return HttpResponse(f"placeholder to display blog number: {number}")

def edit(request, number):
    return HttpResponse(f"placeholder to edit blog number: {number}")

def destroy(request, number):
    return redirect('/blogs')

def jsonResponse(request):
    data = {
        "title": "My First Django Blog",
        "content": "This is some descruption for the blog content..."
    }
    return JsonResponse(data)

def dumpReq(request):
    context = {
        "method": request.method,
        "path": request.path,
        "get_params": dict(request.GET),
        "post_data": dict(request.POST),
        "headers": dict(request.headers),
        "body": request.body.decode("utf-8", errors="ignore"),
        "user": str(request.user),
    }
    return render(request, "dump.html", context)
