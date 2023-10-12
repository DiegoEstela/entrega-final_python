from django.urls import path, include
from django.shortcuts import redirect  # Importa redirect desde django.shortcuts
from django.contrib import admin  # Importa el módulo admin desde django.contrib
from blogapp.views import home
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('', home, name='home'),  # Usa la vista home para la URL raíz
    path('pages/', include('blogapp.urls')),
    path('messages/', include('messaging.urls')),
    path('admin/', admin.site.urls),
]
