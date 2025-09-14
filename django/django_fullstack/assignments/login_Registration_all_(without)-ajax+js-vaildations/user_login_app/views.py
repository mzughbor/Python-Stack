from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from django.contrib import messages
import bcrypt
import datetime

# Create your views here.

def index(request):
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
            
            return redirect("/success")
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
            request.session['user_name'] = f"{user.first_name} {user.last_name}"
            request.session['action'] = 'logged in'
            # Security: Store IP address to detect session hijacking
            request.session['ip_address'] = request.META.get('REMOTE_ADDR')
            
            return redirect("/success")
    return redirect("home")

def logout(request):
    # Use flush() to both clear session data from server side AND delete the session cookie from browser too    
    request.session.flush()
    return redirect("/")

def success(request):
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
    
    context = {
        'user_name': request.session['user_name'],
        'action': request.session['action']
    }
    return render(request, "success.html", context)
