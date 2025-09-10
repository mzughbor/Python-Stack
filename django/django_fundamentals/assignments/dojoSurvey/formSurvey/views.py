from django.shortcuts import render, redirect
#from django.utils import timezone

def index(request):
    return render(request, "index.html")

def create_user(request):
    if request.method == 'POST':
        name_from_form = request.POST['name']
        location_from_form = request.POST['country']
        language_from_form = request.POST['language']
        #status_from_form = request.POST['status']
        status_from_form = request.POST.get('status', 'N/A') 

        comments_from_form = request.POST['comments']
        
        terms_from_form = "Agreed" if 'terms' in request.POST else "Not Agreed"
        
        # Radio button handling (Notification Preferences)
        notifications_from_form = request.POST['notifications'] # name='notifications'

        context = {
            'name_on_template': name_from_form,
            'location_on_template': location_from_form,
            'language_on_template': language_from_form,
            'status_on_template': status_from_form,
            'comments_on_template': comments_from_form,
            'terms_on_template': terms_from_form,
            'notifications_on_template': notifications_from_form,
        }

        if 'context' in request.session:
            return redirect("/success")
        else:
            request.session['context'] = context
            return redirect("result")
    
    else:
        # This block handles initial page load (the GET request) create_user
        return render(request, "index.html")

def result(request):
    return render(request, "result.html")

def success_message(request):
    return render(request, "success.html")
