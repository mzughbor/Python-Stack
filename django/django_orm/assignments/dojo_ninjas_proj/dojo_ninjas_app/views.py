from django.shortcuts import render, redirect
from django.http import HttpResponse 
from dojo_ninjas_app.models import Dojo, Ninja

# Create your views here.
def index(request):
	context = {
		"dojos": Dojo.objects.all(),
		"all_ninjas": Ninja.objects.all()
		}
	return render(request, "index.html", context)


def add_dojo(request):
	if request.method == "POST":
		Dojo.objects.create(
		name=request.POST['name'],
		city=request.POST['city'],
		state=request.POST['state']
	)
	return redirect("home")


def add_ninja(request):
	# dj1 = Dojo.objects.get(id=1)
	# Ninja.objects.create(first_name="..", last_name="...", dojo_name=dj1)
	if request.method == "POST":
		Ninja.objects.create(
			first_name=request.POST['fname'],
			last_name=request.POST['lname'],
			dojo_name= Dojo.objects.get(id=request.POST['dojo'])
		)
	return redirect("home")


def delete_full_dojo_data(request, id):
	if request.method == "POST":
		Dojo.objects.get(id=id).delete()
	return redirect("home")
		
