from django.shortcuts import render
from .models import Post



def index(request):
  post = Post.objects.all()
  context = {
    'object_list' : post
  }
  return render(request, 'index.html', context)

def about(request):
  return render(request, 'about-us.html', {})

def admission(request):
  return render(request, 'admission-form.html', {})

def notice(request):
  return render(request, 'notice-board.html', {})

def result(request):
  return render(request, 'result.html', {})

def routine(request):
  return render(request, 'class-routine.html', {})