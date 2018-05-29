from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm


def logout_view(request):
    logout(request)
    return render(request, 'accounts/logout.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login')
    else:
        form = UserCreationForm()
        context = {
            'form': form,
        }
        return render(request, 'accounts/reg_form.html', context)
