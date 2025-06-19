from django.urls import path
from django.contrib.auth.views import LoginView
# from .views import login

urlpatterns = [
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
]