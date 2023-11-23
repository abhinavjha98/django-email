from django.urls import path
from bummockai.views import index, privacy_policy, terms_of_use, test,send_demo_email

urlpatterns = [
    path('', index, name='index'),
    path('privacy-policy/', privacy_policy, name='privacy_policy'),
    path('terms-of-use/', terms_of_use, name='terms_of_use'),
    path('test/', test, name='test'),
    path('send-demo-email/', send_demo_email, name='send_demo_email'),
    # Add more paths as needed
]
