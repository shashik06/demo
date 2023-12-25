from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def members(request):
    return HttpResponse("hello world")

def home(request):
    return HttpResponse('this is home page')

def about(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
