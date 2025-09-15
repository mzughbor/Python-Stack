from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import User
from django.contrib import messages
import bcrypt
import datetime
import re

# Create your views here.

def index(request):
    if user_id := request.session.get('user_id'):
        return redirect("/books")
    return render(request, "index.html")

def register(request):
    if request.method == "POST":
        errors = User.objects.user_validator(request.POST)
        if errors:
            for key, msg in errors.items():
                messages.error(request, msg)
            return redirect("/")
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
            
            return redirect("/books")
    return redirect("/")

def login(request):
    if request.method == "POST":
        errors = User.objects.user_login_validator(request.POST)
        if errors:
            for key, msg in errors.items():
                messages.error(request, msg)
            return redirect("/")
        else:
            # Get the user
            user = User.objects.get(email=request.POST['email'])
            
            # Store user info in session
            request.session['user_id'] = user.id
            request.session['user_name'] = user.first_name
            request.session['action'] = 'logged in'
            # Security: Store IP address to detect session hijacking
            request.session['ip_address'] = request.META.get('REMOTE_ADDR')

            return redirect("/books")
    return redirect("home")

def logout(request):
    # Use flush() to both clear session data from server side AND delete the session cookie from browser too    
    request.session.flush()
    return redirect("/")



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
