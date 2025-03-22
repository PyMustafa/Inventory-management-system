from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string


def send_welcome_email(user):
    subject = 'Welcome to our Inventory'
    html_message = render_to_string('accounts/emails/welcome.html', {'user': user})  # Pass context if needed

    send_mail(
        subject=subject,
        message='',  # Plain text version
        from_email=None,  # Uses DEFAULT_FROM_EMAIL from settings
        recipient_list=[user.email],
        html_message=html_message,  # HTML version
        fail_silently=True
    )


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                send_welcome_email(user)
                messages.success(request, 'Account created successfully')
                return redirect('login')
            except Exception as e:
                messages.error(request, 'An error occurred')


    else:
        form = UserCreationForm()

    return render(request, 'accounts/register_user.html', {'form': form})

# Create your views here.
