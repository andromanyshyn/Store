from django.contrib.auth.views import LogoutView
from django.urls import path

from users import views

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('profile/<pk>/', views.ProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('verify/<uuid:code>/<int:user_id>/', views.EmailVerification, name='email_verify'),
]