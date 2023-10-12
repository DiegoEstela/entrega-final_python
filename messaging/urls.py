from django.urls import path
from . import views

urlpatterns = [
    path('send/<int:receiver_id>/', views.send_message, name='send_message'),
    path('list/', views.message_list, name='message_list'),
]
