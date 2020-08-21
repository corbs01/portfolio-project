from django.shortcuts import render

from .models import Job

def home(request):
    jobs = Job.objects #Grab everything from the Jobs database
    return render(request, 'jobs/home.html', {'jobs': jobs})
