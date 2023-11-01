from django.urls import path
from blogapp.views import signup, login_view, create_blog, blog_list, blog_detail, about_me, update_user_profile
from django.contrib.auth import views as auth_views
from .views import BlogDeleteView, BlogUpdateView

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('about_me/', about_me, name='about_me'),
    path('pages/', blog_list, name='blog_list'),
    path('pages/<int:blog_id>/', blog_detail, name='blog_detail'),
    path('create/', create_blog, name='create_blog'),
    path('update_profile/', update_user_profile, name='update_profile'),
    path('pages/<int:pk>/delete/', BlogDeleteView.as_view(), name='delete_blog'),
    path('pages/<int:pk>/edit/', BlogUpdateView.as_view(), name='edit_blog'),


]
