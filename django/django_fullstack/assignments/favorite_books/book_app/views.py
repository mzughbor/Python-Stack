from django.shortcuts import render, redirect
#from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from user_login_app.models import User
from .models import Book

# Create your views here.

def index(request):    
    if 'just_deleted' in request.session:
        del request.session['just_deleted']
        messages.success(request, "Book deleted successfully!")

    """ Render the main books page """
    # Check if user is logged in
    if 'user_id' not in request.session:
        return redirect("/")
    # Security: Check for session hijacking by comparing IP addresses
    current_ip = request.META.get('REMOTE_ADDR')
    session_ip = request.session.get('ip_address')
    if session_ip and current_ip != session_ip:
        # Potential session hijacking detected - force logout
        request.session.flush()
        messages.error(request, "Security alert: Session terminated due to suspicious activity.")
        return redirect("/")
    
    user = User.objects.get(id=request.session['user_id'])
    all_books = Book.objects.all().order_by('-created_at')
    liked_books = user.liked_books.all()
    context = {
        'fname' : user.first_name,
        'user_name': request.session['user_name'],
        'action': request.session['action'],
        'current_user': user,
        'all_books' : all_books,
        'liked_books' : liked_books
    }
    return render(request, "books.html", context)

def post_book(request):
    """ Post a new book """
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        if title and title != "" and description and description != "":
            user = User.objects.get(id=request.session['user_id'])
            Book.objects.create(
                title=title,
                description=description,
                uploaded_by=user
            )
            messages.success(request, "Book posted successfully!")
    return redirect("home")

def add_fav(request, id):
    """ Add a book to user's favorites """
    if 'user_id' not in request.session:
        return redirect("/")
    user = User.objects.get(id=request.session['user_id'])
    try:
        book = Book.objects.get(id=id)
        book.users_who_like.add(user)
        messages.success(request, "Book added to your favorites!")
    except Book.DoesNotExist:
        messages.error(request, "Book not found!")
    return redirect("view_book", id=id)

def delete_fav(request, id):
    """ Remove a book from user's favorites """
    if 'user_id' not in request.session:
        return redirect("/")
    user = User.objects.get(id=request.session['user_id'])
    try:
        book = Book.objects.get(id=id)
        book.users_who_like.remove(user)
        messages.success(request, "Book removed from your favorites!")
    except Book.DoesNotExist:
        messages.error(request, "Book not found!")
    return redirect("view_book", id=id)
    
def view_book(request, id):
    """ View details of a specific book and check is it uploaded by current user to allow edit """
    if 'user_id' not in request.session:
        return redirect("/")
    try:
        book = Book.objects.get(id=id)
        user = User.objects.get(id=request.session['user_id'])
        ability = user.books_uploaded.filter(id=id).exists()
        is_liked_this_book = user.liked_books.filter(id=id).exists() # this for sidebar display buttons thing...
        print(is_liked_this_book)
        context = {
            'book': book,
            'books_user_list_likes': book.users_who_like.all(),
            'current_user': user,
            'fname' : user.first_name,
            'user_name': request.session['user_name'],
            'ability': ability,
            'is_liked_this_book': is_liked_this_book
        }
        return render(request, "view_book.html", context)
    except Book.DoesNotExist:
        messages.error(request, "Book not found!")
        return redirect("home")

def update_book(request, id):
    """ Update details of a specific book """
    if request.method == "POST":
        try:
            book = Book.objects.get(id=id)
            title = request.POST['title']
            description = request.POST['description']
            if title and title != "" and description and description != "":
                book.title = title
                book.description = description
                book.save()
                messages.success(request, "Book updated successfully!")
            else:
                messages.error(request, "Title and Description cannot be empty!")
        except Book.DoesNotExist:
            messages.error(request, "Book not found!")
    return redirect("view_book", id=id)

def delete_book(request, id):
    """ Delete a specific book """
    if 'user_id' not in request.session:
        return redirect("/")
    try:
        book = Book.objects.get(id=id)
        user = User.objects.get(id=request.session['user_id'])
        ability = user.books_uploaded.filter(id=id).exists()
        if not ability:
            messages.error(request, "You do not have permission to delete this book!")
            return redirect("home")
        else:
            book.delete()
            request.session['just_deleted'] = True
            
    except Book.DoesNotExist:
        messages.error(request, "Book not found!")
    
    return redirect("home")