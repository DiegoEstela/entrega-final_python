from django.shortcuts import render, get_object_or_404, redirect
from .forms import CustomUserCreationForm, LoginForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib import messages
from .models import Blog, UserProfile


def home(request):
    # Si el usuario está autenticado, redirige a la lista de blogs
    if request.user.is_authenticated:
        return redirect('blog_list')
    else:
        # Si no está autenticado, redirige a la página de inicio de sesión
        return redirect('login')


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Guarda el usuario
            user = form.save()

            # Crea el UserProfile asociado al usuario
            user_profile = UserProfile(
                user=user, username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            user_profile.save()

            # Redirige al login si el registro es exitoso
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificar si el usuario existe en el modelo UserProfile
            try:
                user_profile = UserProfile.objects.get(
                    username=username, password=password)
                if user_profile:
                    # Autenticar y redirigir al usuario si existe
                    user = user_profile.user  # Obtenemos el usuario asociado al UserProfile
                    login(request, user)
                    # Cambia 'home' por la URL que desees después del inicio de sesión
                    return redirect('home')
            except UserProfile.DoesNotExist:
                pass  # El usuario no existe en UserProfile

    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})


class CustomLoginView(LoginView):
    def form_invalid(self, form):
        messages.error(
            self.request, 'Nombre de usuario o contraseña incorrectos. Por favor, inténtelo de nuevo.')
        return super().form_invalid(form)


def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, r'blogapp/blog_list.html', {'blogs': blogs})


def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, r'blogapp/blog_detail.html', {'blog': blog})
