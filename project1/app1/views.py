from django.shortcuts import render, get_object_or_404, redirect
from .models import ABC
from .forms import ABCForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

def index(request):
    return render(request, 'index.html')

def abc_list(request):
    abc_list = ABC.objects.all().order_by('-created_at')
    form = ABCForm()  # empty form to show on the same page
    return render(request, 'abc_list.html', {"abc_list": abc_list, "form": form})

@login_required
def list_create(request):
    if request.method == 'POST':
        form = ABCForm(request.POST, request.FILES)
        if form.is_valid():
            abc = form.save(commit=False)
            abc.user = request.user
            abc.save()
            return redirect('abc_list')
    else:
        form = ABCForm()

    abc_list = ABC.objects.all().order_by('-created_at')
    return render(request, 'abc_form.html', {"form": form, "abc_list": abc_list})

@login_required
def list_edit(request, id):
    abc = get_object_or_404(ABC, pk=id, user=request.user)
    if request.method == 'POST':
        form = ABCForm(request.POST, request.FILES, instance=abc)
        if form.is_valid():
            form.save()
            return redirect('abc_list')
    else:
        form = ABCForm(instance=abc)

    abc_list = ABC.objects.all().order_by('-created_at')
    return render(request, 'abc_form.html', {"form": form, "abc_list": abc_list})

@login_required
def list_delete(request, id):
    abc = get_object_or_404(ABC, pk=id, user=request.user)
    if request.method == 'POST':
        abc.delete()
        return redirect('abc_list')
    return render(request, 'abc_delete.html', {"abc": abc})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {"form": form})

@login_required
def play_video(request, id):
    abc = get_object_or_404(ABC, pk=id)
    return render(request, 'play_video.html', {'abc': abc})