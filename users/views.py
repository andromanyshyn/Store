from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, TemplateView

from common.views import TitleMixin
from products.models import Basket

from .forms import *
from .models import User


class UserLoginView(TitleMixin, LoginView):
    title = 'Store - Login'
    template_name = 'users/login.html'
    form_class = UserLoginForm


class RegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
    title = 'Store - Registration'
    template_name = 'users/registration.html'
    form_class = UserRegistrationForm
    model = User
    success_url = reverse_lazy('login')
    success_message = 'Registration complete successful'


class ProfileView(UpdateView):
    template_name = 'users/profile.html'
    form_class = UserProfileForm
    model = User

    def get_success_url(self):
        return reverse_lazy('profile', args=[self.object.id])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['basket'] = Basket.objects.filter(user=self.request.user)
        return context


def EmailVerification(request, code, user_id):
    email_object = EmailVerifications.objects.filter(code=code, user_id=user_id)
    user = User.objects.get(id=user_id)
    if email_object and email_object.first().is_expired() is False:
        user.is_verified = True
        user.save()

    return render(request, 'users/email_verification.html')
