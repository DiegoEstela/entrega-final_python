from django.urls import path
from blogapp.views import signup, login_view
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('pages/', views.blog_list, name='blog_list'),
    path('pages/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
