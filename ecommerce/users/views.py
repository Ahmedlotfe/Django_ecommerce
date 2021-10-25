from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Your account has been created!, Now you can login")
            return redirect('store')
    else:
        form = UserRegisterForm()
    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)
