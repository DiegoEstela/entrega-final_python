from .forms import CustomUserCreationForm
from .models import UserProfile
from django.shortcuts import render, redirect
from django.contrib.auth import login


def signup(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            login(request, user)

            user_profile = UserProfile(
                user=user,

            )
            user_profile.save()

            return redirect('blog_list')
    else:
        user_form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': user_form})
