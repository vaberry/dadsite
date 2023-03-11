from django.urls import path
from . import views

urlpatterns = [
   path('', views.Home.as_view(), name='home'),
   path("register", views.register_request, name="register"),
   path("login", views.login_request, name="login"),
   path("logout", views.logout_request, name= "logout"),
]