from django.shortcuts import render, redirect
#from django.http import HttpResponse, JsonResponse
from django.contrib import messages

from django.utils import timezone
from datetime import timedelta

from .models import Message, Comment
from user_login_app.models import User

# Create your views here.

def index(request):
    # basically this method was named success in the login/reg app and we clone it and change the rendered file...
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
    all_messages = Message.objects.all().order_by('-created_at')

    thirty_minutes_ago = timezone.now() - timedelta(minutes=30)
    
    # Add can_delete flag to each message
    for message in all_messages:
        message.can_delete = (
            message.user.id == user.id and 
            message.created_at >= thirty_minutes_ago
        )
        """
        # this is an extra attribute added dynamically to the message object so we can use it in the template
        # in other words.
        deletable_messages = []
        for message in all_messages:
            if message.user.id == user.id and message.created_at >= thirty_minutes_ago:
                deletable_messages.append(message.id)
        context = {
            'all_messages': all_messages,
            'deletable_message_ids': deletable_messages
        }
        """
        
    context = {
        'fname' : user.first_name, # added for convenience after clone ..
        'user_name': request.session['user_name'],
        'action': request.session['action'],
        'current_user': user,  # Add current user for delete button logic
        'all_messages' : all_messages
    }
    return render(request, "wall.html", context)

def post_message(request):
    if request.method == "POST":
        message = request.POST['message']
        if message and message != "":
            user = User.objects.get(id=request.session['user_id'])
            Message.objects.create(
                message=message,
                user=user
            )
    return redirect("home")

def post_comment(request, id):
    if request.method == "POST":
        comment = request.POST['comment']
        if comment and comment != "":
            user = User.objects.get(id=request.session['user_id'])
            message = Message.objects.get(id=id)
            Comment.objects.create(
                comment=comment,
                user=user,
                message=message
            )
    return redirect("home")

def delete_message(request, id):
    # Check if user is logged in
    if 'user_id' not in request.session:
        return redirect("/")
    
    try:
        # Get the message and current user
        message = Message.objects.get(id=id)
        current_user = User.objects.get(id=request.session['user_id'])
        
        # Check if the message belongs to the current user
        if message.user.id != current_user.id:
            messages.error(request, "You can only delete your own messages!")
            return redirect("home")
        
        # Check if the message was created within the last 30 minutes
        thirty_minutes_ago = timezone.now() - timedelta(minutes=30)
        if message.created_at < thirty_minutes_ago:
            messages.error(request, "You can only delete messages that are less than 30 minutes old!")
            return redirect("home")
        
        # Delete the message (this will also delete all related comments due to CASCADE)
        message.delete()
        messages.success(request, "Message deleted successfully!")
        
    except Message.DoesNotExist:
        messages.error(request, "Message not found!")
    except Exception as e:
        messages.error(request, "An error occurred while deleting the message.")
    
    return redirect("home")