from django.shortcuts import render, redirect

def index(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1
    
    return render(request, 'index.html')

def destroy(request):
    request.session.flush()
    return redirect('/')

def add_two(request):
    request.session['counter'] = request.session.get('counter', 0) + 1
    return redirect('/')

def reset(request):
    request.session['counter'] = 0
    return redirect('/')

def increment(request):
    if request.method == "POST":
        #num = int(request.form['howMany'])//flask way
        num = int(request.POST['howMany'])
        request.session['counter'] = request.session.get('counter', 0) + num -1
        return redirect('/')
    else:
        return render(request, 'error.html')
