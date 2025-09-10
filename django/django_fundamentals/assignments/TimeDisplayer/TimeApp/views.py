from django.shortcuts import render, HttpResponse 
from time import strftime, gmtime
from datetime import datetime

# from time import gmtime, strftime
# "time": strftime("%Y-%m-%d %H:%M %p", gmtime())


# Create your views here.
def time_display(request):

    current_time = datetime.now()
    
    # Format the datetime object to the desired string format
    # %b: Abbreviated month name (Sep)
    # %d: Day of the month as a zero-padded decimal number (05)
    # %Y: Year with century as a decimal number (2025)
    # %I: Hour (12-hour clock) as a zero-padded decimal number (11)
    # %M: Minute as a zero-padded decimal number (20)
    # %p: Locale’s equivalent of either AM or PM (PM)
        
    time = time.strftime('%I:%M %p', gmtime())
    date = current_time.strftime('%b %d, %Y')
    
    context = {
        "time": time,
        "date": date,
    }
    return render(request,'index.html', context)