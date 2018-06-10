from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
from orders.models import Order,OrderItem

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

def history(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
        item = OrderItem.objects.filter(order__name=username)
    context = {
        'username': username,
        'item': item,
    }
    return render(request, 'accounts/history.html', context)