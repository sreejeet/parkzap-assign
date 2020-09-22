from django.urls import path
from userform_api import views

urlpatterns = [
    path('userdata/', views.UserDataCreateView),
]
