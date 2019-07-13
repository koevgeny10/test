from django.urls import path, include
from . import views

urlpatterns = [
    path(r'registration/', views.RegistrationView.as_view(), name='registration'),
    path('', include('django.contrib.auth.urls'))
]
