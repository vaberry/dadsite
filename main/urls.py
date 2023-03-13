from django.urls import path
from . import views

urlpatterns = [
   path("register", views.register_request, name="register"),
   path("login", views.login_request, name="login"),
   path("logout", views.logout_request, name= "logout"),
   path('', views.Home.as_view(), name='home'),
   path('gallery/', views.Gallery.as_view(), name='gallery'),
   path('story/', views.Story.as_view(), name='story'),
]