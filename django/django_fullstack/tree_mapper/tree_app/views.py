from django.shortcuts import render, redirect
#from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from user_login_app.models import User
from .models import Tree, ZipCode

# Create your views here.

def index(request):    
    if 'just_deleted' in request.session:
        del request.session['just_deleted']
        messages.success(request, "Tree deleted successfully!")

    """ Render the main trees page """
    # Check if user is logged in
    if 'user_id' not in request.session:
        return redirect("home")
    # Security: Check for session hijacking by comparing IP addresses
    current_ip = request.META.get('REMOTE_ADDR')
    session_ip = request.session.get('ip_address')
    if session_ip and current_ip != session_ip:
        # Potential session hijacking detected - force logout
        request.session.flush()
        messages.error(request, "Security alert: Session terminated due to suspicious activity.")
        return redirect("home")
    
    user = User.objects.get(id=request.session['user_id'])
    users = User.objects.all()
    all_trees = Tree.objects.all().order_by('-created_at')
    visited_trees = user.visited_trees.all()
    context = {
        'fname' : user.first_name,
        'user_name': request.session['user_name'],
        'action': request.session['action'],
        'current_user': user,
        'all_trees' : all_trees,
        'visited_trees' : visited_trees,
        'users' : users
    }
    return render(request, "dashboard.html", context)

def new(request):
    """ Post a new tree """
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'fname' : user.first_name,
    }

    if request.method == "GET":
        return render(request, "new_tree.html", context)
    return redirect("home")

def create_tree(request):
    if request.method == "POST":
        if 'user_id' not in request.session:
            return redirect("home")

        # Get all form fields
        species = request.POST.get('species', '').strip()
        notes = request.POST.get('notes', '').strip()
        location = request.POST.get('location', '').strip()
        date_found = request.POST.get('date_found', '')
        zip_code = request.POST.get('zip_codes', '').strip()  # Changed from zip_code to zip_codes to match form
        
        # Validate required fields
        if not all([species, notes, location, date_found, zip_code]):
            messages.error(request, "All fields are required!")
            return redirect("new")

        # Validate and create zip code
        try:
            zip_codes = ZipCode.objects.get(code=zip_code)
        except ZipCode.DoesNotExist:
            zip_codes = ZipCode.objects.create(code=zip_code)
        
        uploaded_by = User.objects.get(id=request.session['user_id'])

        # Validate date format
        try:
            Tree.objects.create(
                species=species,
                location=location,
                date_found=date_found,
                zip_codes=zip_codes,
                notes=notes,
                uploaded_by=uploaded_by
            )
            messages.success(request, "Tree posted successfully!")
            return redirect("home")  # Redirect to dashboard after successful creation
        except Exception as e:
            messages.error(request, f"Error saving tree: {str(e)}")
    return redirect("new")

def add_visit(request, id):
    """ Add a tree to user's visited list """
    if 'user_id' not in request.session:
        return redirect("home")
    user = User.objects.get(id=request.session['user_id'])
    try:
        tree = Tree.objects.get(id=id)
        tree.users_who_like.add(user)
        messages.success(request, "Tree added to your favorites!")
    except Tree.DoesNotExist:
        messages.error(request, "Tree not found!")
    return redirect("view_tree", id=id)

def view_tree(request, id):
    """ View details of a specific tree and check is it uploaded by current user to allow edit """
    if 'user_id' not in request.session:
        return redirect("home")
    try:
        tree = Tree.objects.get(id=id)
        user = User.objects.get(id=request.session['user_id'])
        ability = user.trees_uploaded.filter(id=id).exists()
        is_liked_this_tree = user.visited_trees.filter(id=id).exists() # this for sidebar display buttons thing...
        print(is_liked_this_tree)
        context = {
            'tree': tree,
            'trees_user_list_likes': tree.users_who_like.all(),
            'current_user': user,
            'fname' : user.first_name,
            'user_name': request.session['user_name'],
            'ability': ability,
            'is_liked_this_tree': is_liked_this_tree
        }
        return render(request, "view_tree.html", context)
    except Tree.DoesNotExist:
        messages.error(request, "Tree not found!")
        return redirect("home")

def update_tree(request, id):
    """ Update details of a specific tree """
    if request.method == "POST":
        try:
            tree = Tree.objects.get(id=id)
            title = request.POST['title']
            description = request.POST['description']
            if title and title != "" and description and description != "":
                tree.title = title
                tree.description = description
                tree.save()
                messages.success(request, "Tree updated successfully!")
            else:
                messages.error(request, "Title and Description cannot be empty!")
        except Tree.DoesNotExist:
            messages.error(request, "Tree not found!")
    return redirect("view_tree", id=id)

def delete_tree(request, id):
    """ Delete a specific tree """
    if 'user_id' not in request.session:
        return redirect("home")
    try:
        tree = Tree.objects.get(id=id)
        user = User.objects.get(id=request.session['user_id'])
        ability = user.trees_uploaded.filter(id=id).exists()
        if not ability:
            messages.error(request, "You do not have permission to delete this tree!")
            return redirect("home")
        else:
            tree.delete()
            request.session['just_deleted'] = True
            
    except Tree.DoesNotExist:
        messages.error(request, "Tree not found!")
    
    return redirect("home")