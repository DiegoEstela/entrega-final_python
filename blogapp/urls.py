from django.urls import path
from blogapp.views import signup, login_view, create_blog, blog_list, blog_detail, about_me
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('about_me/', about_me, name='about_me'),
    path('pages/', blog_list, name='blog_list'),
    path('pages/<int:blog_id>/', blog_detail, name='blog_detail'),
    path('create/', create_blog, name='create_blog'),
]
