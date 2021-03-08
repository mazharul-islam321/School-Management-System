from django.shortcuts import render






def index(request):
  return render(request, 'index.html', {})

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