from django.urls import path
from management import views

urlpatterns = [
    path('contact/', views.contactUs, name='contact')
]