from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm

def logout_view(request):
    logout(request)
    return render(request, 'accounts/logout.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login')
    else:
        form = RegistrationForm()
        context = {
            'form': form,
        }
        return render(request, 'accounts/reg_form.html', context)
def profile(request):

    context = {
        'user': request.user,
    }
    return render(request, 'accounts/profile.html')