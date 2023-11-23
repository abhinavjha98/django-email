from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import json
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    return render(request, 'index.html')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

def terms_of_use(request):
    return render(request, 'terms-of-use.html')

def test(request):
    return render(request, 'test.html')

def send_demo_email(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        first_name = data.get('firstName')
        lastName = data.get('lastName')
        email = data.get('email')
        message = data.get('message')

        # Send email using Django's send_mail
        send_mail(
            subject="Demo Request",
            message=f"Name: {first_name} {lastName}\nEmail: {email}\nMessage: {message}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['recipient@example.com'],
        )

        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'error'}, status=400)