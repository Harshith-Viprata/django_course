from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
    return HttpResponse('hello world')

def item(request):
    return HttpResponse('This is an Item view')

