from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import TVShow
from django.http import JsonResponse


def ajax_create_show(request):
    if request.method == "POST":
        errors = TVShow.objects.basic_validator(request.POST)
        if errors:  # validation failed
            return JsonResponse({"errors": errors}, status=400)

        show = TVShow.objects.create(
            title=request.POST["title"],
            network=request.POST["network"],
            release_date=request.POST["release_date"],
            desc=request.POST["desc"],
        )

        return JsonResponse({
            "id": show.id,
            "title": show.title,   # ✅ include title to fix "Saved: undefined"
        })

    return JsonResponse({"error": "Invalid request"}, status=405)


def ajax_update_show(request, id):
    show = get_object_or_404(TVShow, id=id)

    if request.method == "POST":
        # Make a mutable copy of POST and add the show_id
        post_data = request.POST.copy()
        post_data['show_id'] = str(id)

        errors = TVShow.objects.basic_validator(post_data)
        if errors:  # validation failed
            return JsonResponse({"errors": errors}, status=400)

        # If no errors, update fields
        show.title = request.POST["title"]
        show.network = request.POST["network"]
        show.release_date = request.POST["release_date"]
        show.desc = request.POST["desc"]
        show.save()

        return JsonResponse({
            "message": "Updated successfully",
            "id": show.id,
            "title": show.title,
        })

    return JsonResponse({"error": "Invalid request"}, status=405)


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
        
        # Create a copy of POST data to add pk so we git rid of error duplicated with current one...
        post_data = request.POST.copy()
        post_data['pk'] = id
        
        # Run validations with pk included
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
