from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterUserForm

def register(request):
    form = RegisterUserForm()

    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid(form):
            form.save()
            messages.success(request, f"Account have been created!")
            return redirect('front')
    else:
        form = RegisterUserForm()

    context = {
        'form' : form
    }

    return render(request, 'users/register.html', context)