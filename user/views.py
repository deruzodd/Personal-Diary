from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from .forms import RegisterForm, LoginForm, UserConfigForm
from .models import UserModel
from diary.models import DiaryEntry

def index(request):
    if (request.user.is_authenticated):
        return redirect('dashboard')
    return render(request, 'user/index.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
          user = form.save(commit=False)
          user.save()
          auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
          return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'user/register.html', {'form': form})

@login_required
def login(request):
    form = LoginForm()
    return render(request, 'user/login.html', {'form': form})

@login_required
def user_config(request):
    if request.method == 'POST':
        form = UserConfigForm(request.POST)
        if form.is_valid():
            request.user.theme = form.cleaned_data['theme']
            request.user.font_size = form.cleaned_data['font_size']
            request.user.save()
            return redirect('dashboard')
    # else:
    #     form = UserConfigForm(initial={'theme': request.user.theme})
    # return render(request, 'user/user_config.html', {'form': form})

def demo_login(request):
    # generate a fresh Demo user
    try:
        user = UserModel.objects.get(username='Guest')
        entries = DiaryEntry.objects.filter(author=user)
        for entry in entries:
            entry.delete()
        user.delete()
    except UserModel.DoesNotExist:
        pass
    user = UserModel.objects.create_user(username='Guest', password='xHedBJPBYNSbjhCB')
    user.is_demo = True
    user.save()

    auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
    return redirect('dashboard')
