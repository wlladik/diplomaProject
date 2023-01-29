from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegForm, UserUpdateForm, ProfileImageForm, SexForm, BoolForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method =="POST":
        form = UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'User {username} was successfully added!')
            return redirect('home')
    else:
        form = UserRegForm()

    return render(
        request,
        'users/registration.html',
        {
        'title': 'Registration page',
        'form': form

        }
    )

@login_required
def profile(request):
    if request.method=="POST":
        profileForm = ProfileImageForm(request.POST, request.FILES, instance=request.user.profile)
        updateUserForm = UserUpdateForm(request.POST, instance=request.user)
        updateSexForm = SexForm(request.POST, instance=request.user.profile)
        updateBool = BoolForm(request.POST, instance=request.user.profile)

        if profileForm.is_valid() and updateUserForm.is_valid() and updateSexForm.is_valid():
            updateUserForm.save()
            profileForm.save()
            updateSexForm.save()
            updateBool.save()
            messages.success(request, f'Your account was successfuly updated!')
            return redirect('profile')
    else:
        profileForm = ProfileImageForm(instance=request.user.profile)
        updateUserForm = UserUpdateForm(instance=request.user)
        updateSexForm = SexForm(instance=request.user.profile)
        updateBool = BoolForm(instance=request.user.profile)

    data = {
        'profileForm': profileForm,
        'updateUserForm': updateUserForm,
        'updateSexForm': updateSexForm,
        'updateBool': updateBool
    }

    return render(request, 'users/profile.html', data)
