from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import User
from django.contrib import messages
import bcrypt
import datetime
import re
from .models import User, Tree, ZipCode, Visit

# Create your views here.

def index(request):
    if 'user_id' in request.session:
        return redirect("dashboard")
    return render(request, "index.html")

def register(request):
    if request.method == "POST":
        errors = User.objects.user_validator(request.POST)
        if errors:
            for key, msg in errors.items():
                messages.error(request, msg)
            return redirect("home")
        else:
            # Hash the password with bcrypt before saving
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            
            # Convert birthday string to date object
            birthday = datetime.datetime.strptime(request.POST['birthday'], '%Y-%m-%d').date()
            
            # Create the user
            user = User.objects.create(
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST['email'],
                password=pw_hash,
                birthday=birthday
            )
            
            # Store user info in session
            request.session['user_id'] = user.id
            request.session['user_name'] = f"{user.first_name} {user.last_name}"
            request.session['action'] = 'registered'
            # Security: Store IP address to detect session hijacking
            request.session['ip_address'] = request.META.get('REMOTE_ADDR')
            
            return redirect("/dashboard")    
    return redirect("home")


def login(request):
    if request.method == "POST":
        errors = User.objects.user_login_validator(request.POST)
        if errors:
            for key, msg in errors.items():
                messages.error(request, msg)    
            return redirect("home")

        else:
            # Get the user
            user = User.objects.get(email=request.POST['email'])
            
            # Store user info in session
            request.session['user_id'] = user.id
            request.session['user_name'] = f"{user.first_name} {user.last_name}"
            request.session['action'] = 'logged in'
            # Security: Store IP address to detect session hijacking
            request.session['ip_address'] = request.META.get('REMOTE_ADDR')
            
            return redirect("/dashboard")
    return redirect("home")

def logout(request):
    # Use flush() to both clear session data from server side AND delete the session cookie from browser too    
    request.session.flush()
    return redirect("home")

def success(request):
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
    all_trees = Tree.objects.all().order_by('-created_at')
    context = {
        'fname' : user.first_name, #
        'user_name': request.session['user_name'],
        'action': request.session['action'], # extra new user or not ...
        'current_user': user,
        'user_trees': user.creates.all(),
        'all_trees' : all_trees
    }
    return render(request, "dashboard.html", context)

def check_email(request):
    """AJAX view to check email uniqueness and format"""
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        
        # Email format validation
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+$')
        
        if not email:
            return JsonResponse({
                'valid': False,
                'message': 'Email is required.',
                'color': 'red'
            })
        elif not EMAIL_REGEX.match(email):
            return JsonResponse({
                'valid': False,
                'message': 'Please enter a valid email format.',
                'color': 'red'
            })
        elif User.objects.filter(email=email).exists():
            return JsonResponse({
                'valid': False,
                'message': 'This email is already registered.',
                'color': 'red'
            })
        else:
            return JsonResponse({
                'valid': True,
                'message': 'Email is available!',
                'color': 'green'
            })
    
    return JsonResponse({'error': 'Invalid request'})


def new_tree_form(request):
    if 'user_id' not in request.session:
        return redirect("home")

    user = User.objects.get(id=request.session['user_id'])
    context = {
        'fname' : user.first_name,
        'user_name': request.session['user_name'],
        'action': request.session['action'], # extra new user or not ...
        'current_user': user,
    }
    return render(request, "add-tree.html", context)

"""
def post_tree_req(request):
    if request.method == "POST":
        
        species = request.POST.get('species', '').strip() # don't do >> species = request.POST['species'] only
        location = request.POST.get('location', '').strip()
        date_found_str = request.POST.get('dateFound', '')
        notes = request.POST.get('notes', '').strip()
        zip_code_from_form = request.POST.get('zipCode', '').strip()

        if not species or not location or not date_found_str or not zip_code_from_form:
            messages.error(request, "All fields are required.")
            return redirect("new_tree_form")
            
        if len(notes) > 50:
            messages.error(request, "Notes must not exceed 50 characters.")
            return redirect("new_tree_form")

        if len(species) < 2:
            messages.error(request, "Species must be at least 2 characters.")
            return redirect("new_tree_form")

        if len(location) < 5:
            messages.error(request, "Address must be at least 5 characters.")
            return redirect("new_tree_form")

        try:
            date_found = datetime.datetime.strptime(request.POST['dateFound'], '%Y-%m-%d').date()
            # this checks the vaildation of the date if it's new or not 
            if date_found > datetime.date.today():
                messages.error(request, "Date cannot be in the future.")
                return redirect("new_tree_form")
        except (ValueError, KeyError):
            messages.error(request, "Invalid date format.")
            return redirect("new_tree_form")
        
        #zip_code_from_form = request.POST['zipCode']                       # striped above
        #createZipCode = ZipCode.objects.create(code=zip_code_from_form)
        #zipcode = ZipCode.objects.get(code=zip_code_from_form)
        # creates duplicates..
        zipcode, created = ZipCode.objects.get_or_create(code=zip_code_from_form)

        if 'user_id' not in request.session: # we must have registerd user
            messages.error(request, "You must be logged in to add a tree.")
            return redirect("home")

        #species = request.POST.get('species', '').strip() # this will solve the MultiValueDictKeyError if user leve empty or didn't change the default value.

        if species.strip() and location.strip() and notes.strip(): # alone creates issue like MultiValueDictKeyError so you have 
            user = User.objects.get(id=request.session['user_id'])
            Tree.objects.create(
                species=species,
                notes=notes,
                created_by=user,
                date_found=date_found,
                location=location,
                zip_code= zipcode
            )
            messages.success(request, "Tree created successfully!")
    return redirect("home")
"""

def post_tree_req(request):
    if request.method != "POST":
        return redirect("new_tree_form")

    species = request.POST.get('species', '').strip()
    location = request.POST.get('location', '').strip()
    date_found_str = request.POST.get('dateFound', '').strip()
    notes = request.POST.get('notes', '').strip()   # ✅ keep this
    zip_code_from_form = request.POST.get('zipCode', '').strip()

    errors = {}

    # Required fields
    if not species or not location or not date_found_str or not zip_code_from_form or not notes:
        errors['required'] = "All fields are required."

    # Species length
    if len(species) < 2:
        errors['species'] = "Species must be at least 2 characters."
    elif len(species) > 255:
        errors['species'] = "Species must not exceed 255 characters."

    # Location length
    if len(location) < 5:
        errors['location'] = "Address must be at least 5 characters."
    elif len(location) > 255:
        errors['location'] = "Address must not exceed 255 characters."

    # Notes length
    if len(notes) == 0:
        errors['notes'] = "Notes cannot be empty."
    elif len(notes) > 50:
        errors['notes'] = "Notes must not exceed 50 characters."

    # Date validation
    try:
        date_found = datetime.datetime.strptime(date_found_str, '%Y-%m-%d').date()
        if date_found > datetime.date.today():
            errors['date'] = "Date cannot be in the future."
    except ValueError:
        errors['date'] = "Invalid date format. Use YYYY-MM-DD."

    # Zip code check
    if not re.fullmatch(r"\d{5}", zip_code_from_form):
        errors['zip'] = "Zip code must be a 5-digit number."

    # If errors, redirect back
    if errors:
        for msg in errors.values():
            messages.error(request, msg)
        return redirect("new_tree_form")

    # Ensure user is logged in
    if 'user_id' not in request.session:
        messages.error(request, "Login required to add a tree.")
        return redirect("home")

    user = User.objects.get(id=request.session['user_id'])
    zipcode, created = ZipCode.objects.get_or_create(code=zip_code_from_form)

    Tree.objects.create(
        species=species,
        location=location,
        date_found=date_found,
        notes=notes,
        zip_code=zipcode,
        created_by=user
    )

    messages.success(request, "Tree added successfully!")
    return redirect("dashboard")

def delete_tree(request, id):
    if 'user_id' not in request.session:
        return redirect("/")
    try:
        tree = Tree.objects.get(id=id)
        user = User.objects.get(id=request.session['user_id'])
        # authorization check
        ability = user.creates.filter(id=id).exists()
        if not ability:
            messages.error(request, "You do not have permission to delete this tree!")
            return redirect("home")
        else:
            tree.delete()
            messages.success(request, "Tree deleted successfully!")
            
    except Tree.DoesNotExist:
        messages.error(request, "Tree not found!")
    
    return redirect("home")

def edit_tree(request, id):
    """ Update details of a specific tree """
    if 'user_id' not in request.session:
        return redirect("home")
    elif 'user_id' not in request.session:
        return redirect("home")
    # check authorization
    user = User.objects.get(id=request.session['user_id'])
    if not user.creates.filter(id=id).exists():
        messages.error(request, "You do not have permission to edit this tree.")
        return redirect("dashboard")

    try:
        tree = Tree.objects.get(id=id)
    except Tree.DoesNotExist:
        messages.error(request, "Tree not found.")
        return redirect("dashboard")

    if request.method == "POST":
        species = request.POST.get('species', '').strip()
        location = request.POST.get('location', '').strip()
        date_found_str = request.POST.get('dateFound', '')
        notes = request.POST.get('notes', '').strip()
        zip_code_from_form = request.POST.get('zipCode', '').strip()

        # ✅ fallback to old values if empty
        species = species if species else tree.species
        location = location if location else tree.location
        notes = notes if notes else tree.notes
        zip_code_from_form = zip_code_from_form if zip_code_from_form else tree.zipCode
        date_found_str = date_found_str if date_found_str else tree.dateFound.strftime("%Y-%m-%d")

        # validate
        errors = {}

        if not species or not location or not date_found_str or not zip_code_from_form:
            messages.error(request, "All fields are required.")
            return redirect("edit_tree_form", id=id)
        
        if len(species) < 2:
            errors['species'] = "Species must be at least 2 characters."
        if len(location) < 5:
            errors['location'] = "Location must be at least 5 characters."
        if len(notes) > 50:
            errors['notes'] = "Notes must not exceed 50 characters."
        
        if errors:
            for key, msg in errors.items():
                messages.error(request, msg)
            return redirect("edit_tree_form", id=id)

        try:
            date_found = datetime.datetime.strptime(date_found_str, '%Y-%m-%d').date()
            if date_found > datetime.date.today():
                messages.error(request, "Date cannot be in the future.")
                return redirect("edit_tree_form", id=id)
        except ValueError:
            messages.error(request, "Invalid date format.")
            return redirect("edit_tree_form", id=id)

        if not re.fullmatch(r"\d{5}", zip_code_from_form):
            messages.error(request, "Zip code must be a 5-digit number.")
            return redirect("edit_tree_form", id=id)

        if 'user_id' not in request.session:
            messages.error(request, "You must be logged in to edit a tree.")
            return redirect("home")

        zipcode, created = ZipCode.objects.get_or_create(code=zip_code_from_form)

        tree.species = species
        tree.notes = notes
        tree.date_found = date_found
        tree.location = location
        tree.zip_code = zipcode
        tree.save()

        messages.success(request, "Tree updated successfully!")
        return redirect("dashboard")

    # For GET request, render form with current tree data
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'tree': tree,
        'fname' : user.first_name,
        'user_name': request.session['user_name'],
        'action': request.session['action'], # extra new user or not ...
        'current_user': user,
    }    
    return render(request, "edit_tree.html", context)

def view_tree(request, id):
    if 'user_id' not in request.session:
        return redirect("home")
    try:
        tree = Tree.objects.get(id=id)
    except Tree.DoesNotExist:
        messages.error(request, "Tree not found.")
        return redirect("dashboard")
    try:
        tree = Tree.objects.get(id=id)
        current_user = User.objects.get(id=request.session['user_id'])
        visited = Visit.objects.filter(user=current_user, tree=tree).exists()
        return render(request, "view_tree.html", {
            "tree": tree,
            "visited": visited,
            "visited_users" : tree.visits.all(),
            "fname" : current_user.first_name,
            "ser_name": request.session['user_name'],
            "action": request.session['action'],
            "current_user": current_user,
        })
    except Tree.DoesNotExist:
        messages.error(request, "Tree not found.")
        return redirect("dashboard")


def toggle_visit(request, id):
    if 'user_id' not in request.session:
        return redirect("home")
    try:
        tree = Tree.objects.get(id=id)
        user = User.objects.get(id=request.session['user_id'])

        visit = Visit.objects.filter(user=user, tree=tree).first()

        if visit:
            # If a visit exists → remove it
            visit.delete()
            messages.success(request, "Visit removed.")
        else:
            # If no visit exists → create it
            Visit.objects.create(user=user, tree=tree)
            messages.success(request, "Tree marked as visited!")
    except Tree.DoesNotExist:
        messages.error(request, "Tree not found.")

    return redirect("view_tree", id=id)
