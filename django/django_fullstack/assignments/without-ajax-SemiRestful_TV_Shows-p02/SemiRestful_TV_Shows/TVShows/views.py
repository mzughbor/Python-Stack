from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from .models import TVShow

# Create your views here.
def root(request):
    return redirect('/shows')

def index(request):
    shows = TVShow.objects.all().order_by('-created_at')
    return render(request, 'read-all.html', {'shows': shows})

def new(request):
    return render(request, 'create.html')

def create(request):
    if request.method == 'POST':
        
        # Run validations
        errors = TVShow.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/shows/new')
                
        show = TVShow.objects.create(
            title=request.POST['title'],
            network=request.POST['network'],
            release_date=request.POST['release_date'],
            desc=request.POST['desc']
        )
        #messages.success(request, "Show successfully created!")        
        request.session['success'] = f"<strong>{show.title}</strong> has been successfully added!"
        return redirect(f'/shows/{show.id}')

    return redirect('/shows/new')

def show(request, id):
    show = TVShow.objects.get(id=id)
    context = {
        'show': show,
        'success': request.session.get('success', None)
    }
    if 'success' in request.session:
        del request.session['success']  # clear the message after showing it
    return render(request, 'read-one.html', context)

def edit(request, id):
    show = TVShow.objects.get(id=id)
    return render(request, 'update.html', {'show': show})

def update(request, id):
    show = TVShow.objects.get(id=id)
    if request.method == 'POST':
        
        # Create a copy of POST data to add show_id so we git rid of error duplicated with current one...
        post_data = request.POST.copy()
        post_data['show_id'] = id
        
        # Run validations with show_id included
        errors = TVShow.objects.basic_validator(post_data)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/shows/{id}/edit')
        
        # If no errors update right away
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['release_date']
        show.desc = request.POST['desc']
        show.save()
        request.session['success'] = f"<strong>{show.title}</strong> has been successfully updated!"
        return redirect(f'/shows/{id}')
    return redirect('/shows')

def destroy(request, id):
    show = TVShow.objects.get(id=id)
    if request.method == 'POST':
        show.delete()
    return redirect('/shows')
