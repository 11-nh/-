from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def zhanshi(request):
    return render(request,'algorithms/index.html')