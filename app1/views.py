from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.views.generic import DetailView
from app1.models import Server,User

# Create your views here.


def index(request):
    list_my = Server.objects.order_by('id')
    return HttpResponse(list_my)
def server(request):
    return HttpResponse("Hello. You are at the server page.")
def user(request):
    return HttpResponse("Hello. You are at the user page.")
