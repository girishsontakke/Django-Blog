from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from user.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Account Created for {username}!, Now you can log in.")
            return redirect("user:login")

    else:
        form = UserRegisterForm()
    return render(request, "user/register.html", {'form': form})


@login_required
def profile(request):
    if request.method == "GET":
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    else:
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Your Profile has been updated 🚀")
            return redirect("user:profile")

    context = {
        "u_form": u_form,
        "p_form": p_form
    }
    return render(request, "user/profile.html", context)
