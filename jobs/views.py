from django.shortcuts import render
from django.http import HttpResponse
from .models import Jobs,Personal

# Create your views here.
def index(request):
    return render(request,'index.html')
def job_description(request):
    dict_jobs={
        'jobs':Jobs.objects.all()
    }
    return render(request,'jobs.html',dict_jobs)
    # return HttpResponse("desc")
def personal_details(request):
    dict_persons={
        'person':Personal.objects.all()
    }
    return render(request,'person.html',dict_persons)
    