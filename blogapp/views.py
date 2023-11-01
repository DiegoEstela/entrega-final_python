from django.shortcuts import render, get_object_or_404, redirect
from .forms import CustomUserCreationForm, LoginForm, BlogForm, UserProfileUpdateForm
from django.contrib.auth import login
from .models import Blog, UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .models import Blog
from django.views.generic.edit import UpdateView


def home(request):
    if request.user.is_authenticated:
        return redirect('blog_list')
    else:
        return redirect('login')


def about_me(request):
    return render(request, 'blogapp/about_me.html')


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            user.save()
            user_profile = UserProfile(
                user=user, username=form.cleaned_data['username'], password=form.cleaned_data['password1'], email=form.cleaned_data['email'])
            user_profile.save()

            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(email=email)
                if user.check_password(password):
                    login(request, user)
                    return redirect('home')
            except User.DoesNotExist:
                messages.error(request, 'Credenciales inválidas.')

    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})


def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blogapp/blog_list.html', {'blogs': blogs})


def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blogapp/blog_detail.html', {'blog': blog})


@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('blog_list')
    else:
        form = BlogForm()

    return render(request, 'blogapp/create_blog.html', {'form': form})


@login_required
def update_user_profile(request):
    if request.method == 'POST':
        form = UserProfileUpdateForm(
            request.POST, instance=request.user.userprofile)

        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('home'))

    else:
        form = UserProfileUpdateForm(instance=request.user.userprofile)

    return render(request, 'registration/update_profile.html', {'form': form})


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blogapp/blog_confirm_delete.html'
    success_url = reverse_lazy('blog_list')


class BlogUpdateView(UpdateView):
    model = Blog
    template_name = 'blogapp/edit_blog.html'
    form_class = BlogForm
    success_url = reverse_lazy('blog_list')
