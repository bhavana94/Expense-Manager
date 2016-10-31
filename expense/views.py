from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .models import Account, Category, Transactions
from .forms import UserForm

# Create your views here.


def helloworld(request):

    return render(request, 'index.html')


def credit(request):

    return render(request, 'credit.html')


def debit(request):

    return render(request, 'debit.html')


def history(request):

    return render(request, 'history.html')


def login_user(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                account = Account.objects.filter(user=request.user)
                return render(request, 'index.html')
            else:
                return render(request, 'login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'login.html', {'error_message': 'Invalid Login'})
    else:
        return render(request, 'login.html')

def logout_user(request):

    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form":form
    }
    return render(request, 'login.html', context)


def register(request):

    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'index.html')

    context = {
    "form": form
    }

    return render(request, 'register.html', context)
