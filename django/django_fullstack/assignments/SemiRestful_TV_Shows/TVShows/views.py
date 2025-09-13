from django.shortcuts import render, redirect, get_object_or_404
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
        show = TVShow.objects.create(
            title=request.POST['title'],
            network=request.POST['network'],
            release_date=request.POST['release_date'],
            desc=request.POST['desc']
        )
        return redirect(f'/shows/{show.id}')
    return redirect('/shows/new')

def show(request, id):
    show = TVShow.objects.get(id=id)
    return render(request, 'read-one.html', {'show': show})

def edit(request, id):
    show = TVShow.objects.get(id=id)
    return render(request, 'update.html', {'show': show})

def update(request, id):
    show = TVShow.objects.get(id=id)
    if request.method == 'POST':
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['release_date']
        show.desc = request.POST['desc']
        show.save()
        return redirect(f'/shows/{id}')
    return redirect('/shows')

def destroy(request, id):
    show = TVShow.objects.get(id=id)
    if request.method == 'POST':
        show.delete()
    return redirect('/shows')
