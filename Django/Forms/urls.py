from django.urls import path
from Forms import views

urlpatterns = [
    path('signup/',views.sign_up),
]
