from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard.html', {})

def icons(request):
    return render(request, 'icons.html', {})

def notification(request):
    return render(request, 'notifications.html', {})

def tables(request):
    return render(request, 'tables.html', {})

def user(request):
    return render(request, 'user.html', {})


