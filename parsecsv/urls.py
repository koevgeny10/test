from django.urls import path
from . import views

urlpatterns = [
    path(r'1/', views.FirstPage.as_view(), name='firstpage'),
    path(r'2/', views.SecondPage.as_view(), name='secondpage')
]
