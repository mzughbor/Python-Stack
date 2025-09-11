from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .models import Book, Author

# Create your views here.
def root(request):
	context = {
		"all_books" : Book.objects.all()
	}
	return render(request, "book.html", context)

def add_new_book(request):
	if request.method == "POST":
		new_title = request.POST['bookTitle']
		new_desc = request.POST['bookDescription']
		Book.objects.create(title=new_title, desc=new_desc)
	return redirect("home")

def book_details(request, id):
	context = {
		"book" : Book.objects.get(id=id),
		"other_authors" : Author.objects.exclude(books=id),
	}
	return render(request, "book-details.html", context)

def add_author(request, id):
	if request.method == "POST":
		author_id = request.POST['author_id']
		
		if author_id and author_id != "":		
			new_author = Author.objects.get(id=author_id)
			book_we_are_in = Book.objects.get(id=id)
			book_we_are_in.authors.add(new_author)
		else:
			return redirect("home")

	return redirect("book_details", id)

def author(request):
	context = {
		"all_author" : Author.objects.all()
	}
	return render(request, "author.html", context)

def add_new_author(request):
	if request.method == "POST":
		firstname = request.POST['firstname']
		lastname = request.POST['lastname']
		Notes = request.POST['Notes']
		Author.objects.create(first_name=firstname, last_name=lastname, notes=Notes)
	return redirect("authors")

def author_details(request, id):
	context = {
		"author" : Author.objects.get(id=id),
		"other_books" : Book.objects.exclude(authors=id),
	}
	return render(request, "author-details.html", context)

def add_book(request, id):
	if request.method == "POST":
		book_id = request.POST['book_id']
		
		if book_id and book_id != "":		
			new_book = Book.objects.get(id=book_id)
			author_we_are_in = Author.objects.get(id=id)
			author_we_are_in.books.add(new_book)
		else:
			return redirect("home")

	return redirect("author_details", id)
	