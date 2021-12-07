from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    # return HttpResponse("Hello World !")
    developed_by = "Jaymin patel"
    mentors = [
        "Pratik Narang",
        "Ravi Patel",
        "Suresh Raina",
        "Piyush j. patel",
        "Chirag Patel"
    ]

    context = {
        "developer":developed_by,
        "mentors": mentors
    }
    
    return render(request,'HelloWorld/index.html',context)