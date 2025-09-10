from django.shortcuts import render, redirect
from time import strftime, localtime
import random
from django.contrib import messages

# Create your views here.

def root(request):
    if 'activities' not in request.session:
        request.session['activities'] = []
        request.session['gold'] = 0
    
    context = {
        "gold": request.session['gold'],
        "activities": request.session['activities']
    }
    return render(request, 'index.html', context)


def process_money(request):

    # Get the current local time as a formatted string
    current_time = strftime("%Y-%m-%d %H:%M %p", localtime())
    adapter = random.randint(0,3)
    # in case 0 >> he gonna lose the 50 in quest
    # in others >> he gonna get random 5, 10, 15 based on that variable 
    our_gold = {
        0 : -50,
        1 : 10,
        2 : 12,
        3 : 15,
        4 : 20
    }
    
    if request.method == "POST":
        
        if adapter == 0 and request.POST['building'] == "quest":        
            request.session['gold'] -= 50
            request.session['activities'].append(f'You faild a quest and lost 50 gold. {current_time}')

        # this only for when decrease the score, to forece it restart again. score in miuns
        if request.session['gold'] < 0:
            # Add a message to be displayed on the next page
            messages.error(request, 'Your gold has fallen below zero! Game over. Please start a new game.')
            redirect('reset')
            return redirect('home')

        # all normal + cases  / where the 0 is not needed to be selected randomly at all              
        if adapter == 0:
            adapter += 1
        else:
            pass
        
        if request.POST['building'] == "farm":            
            request.session['gold'] += our_gold[adapter]
            request.session['activities'].append(f'You entered a farm and earned {our_gold[adapter]} gold. ({current_time})')
        
        elif request.POST['building'] == "cave":
            request.session['gold'] += our_gold[adapter]
            request.session['activities'].append(f'You entered a cave and earned {our_gold[adapter]} gold. ({current_time})')
        
        elif request.POST['building'] == "house":
            request.session['gold'] += our_gold[adapter]
            request.session['activities'].append(f'You entered a house and earned {our_gold[adapter]} gold. ({current_time})')
        
        elif request.POST['building'] == "quest":
            value = random.randint(25,30)
            request.session['gold'] += value
            request.session['activities'].append(f'You completed a quest and earned {value} gold. ({current_time})')
        
        else:
            request.session['activities'].append(f'You are trying to cheat! ({current_time})')     
            
    return redirect('home')


def reset(request):
    request.session.flush()        
    return redirect('home')
