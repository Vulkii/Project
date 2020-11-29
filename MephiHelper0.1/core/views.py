from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import permission_required




def about(request):
    return render(request, 'core/about.html')

def math(request):
    return render(request,'core/math.html')

def course(request):
    return render(request,'core/1 course.html')

def coursee(request):
    return render(request,'core/2 course.html')

def helpers(request):
    return render(request,'core/helpers.html')



def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'core/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'core/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')

def events(request):
    tasks = Task.objects.all()
    return render(request, 'core/events.html', {'tasks' : tasks})

def create(request):
    error = ''
    if request.method == 'POST'  :
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'core/create.html', context)