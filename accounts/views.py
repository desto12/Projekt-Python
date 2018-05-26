from django.shortcuts import render
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return render(request, 'accounts/logout.html')

def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        ...