from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

meetups = [
    {'title': 'Hi, My Name is Zain'},
    {'profession': 'Hi, I am a Full Stack Software Engineer'}
]

def index(request):
    return render(request, 'meetups/index.html',{
        'meetups':meetups,
        'meetUpOn': True
    })
