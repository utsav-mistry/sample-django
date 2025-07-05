from django.http import HttpResponse
from django.shortcuts import render,request

def index(request):
    return render(request,'test.html')
