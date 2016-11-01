from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Account, Category, Transactions
from .forms import UserForm, AccountForm

# Create your views here.


def helloworld(request):
    form = AccountForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        amount = form.cleaned_data['amount']
        category = form.cleaned_data['category']
        transaction_type = form.cleaned_data['transaction_type']
        comment = form.cleaned_data['comment']
        account = form.cleaned_data['account']
        user.save()
        if user is not None:
            if user:
                cat = Category.objects.all()
                return render(request, 'index.html', {'cat': cat})

    context = {
        "form": form
    }

    return render(request, 'index.html', context)



def credit(request):

    return render(request, 'credit.html')


@login_required
@csrf_protect
def profile(request):

    if request.method == "POST":
        form = UserForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            account = Account.objects.filter(user=request.user)
            return render(request, 'profile.html', {'account': account})
    else:
        user = request.user
        profile = user.profile
        form = UserForm(instance=profile)

    args = {}
    args['form'] = form
    return render(request, 'profile.html', args)


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
                return render(request, 'profile.html')
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
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'index.html')

    context = {
        "form": form
    }

    return render(request, 'register.html', context)
