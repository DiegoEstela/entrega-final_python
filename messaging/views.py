from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Message


@login_required
def send_message(request, receiver_id):
    if request.method == 'POST':
        content = request.POST.get('content', '')
        receiver = get_object_or_404(User, pk=receiver_id)
        message = Message.objects.create(
            sender=request.user, receiver=receiver, content=content)
        return redirect('message_list')
    else:
        return render(request, 'messaging/send_message.html')


@login_required
def message_list(request):
    messages = Message.objects.filter(receiver=request.user)
    return render(request, 'messaging/message_list.html', {'messages': messages})
