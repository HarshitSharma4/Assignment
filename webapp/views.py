from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from .models import User


def index(request):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render(request, 'webapp/index.html', {'time': current_time})

def submit(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        new_user = User(name=name, email=email)
        new_user.save()
        return redirect('users')

def users(request):
    users = User.objects.all()
    return render(request, 'webapp/users.html', {'users': users})
