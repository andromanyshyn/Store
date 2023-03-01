from datetime import timedelta

from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.mail import send_mail
from django.urls import reverse

from store import settings


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    is_verified = models.BooleanField(default=False)


class EmailVerifications(models.Model):
    user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
    code = models.UUIDField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()

    def __str__(self):
        return f'EmailVerification for {self.user_id.username}'

    def sending_email(self):
        DOMAIN = 'http://127.0.0.1:8000'
        link = reverse('email_verify', kwargs={'code': self.code, 'user_id': self.user_id.id})
        send_link = f'Dear {self.user_id.username}! For verify ' \
                    f'your account please go to the link {DOMAIN}{link}'
        subject = 'Store - Email Verification'
        send_mail(
            subject=subject,
            message=send_link,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.user_id.email]
        )

    def is_expired(self):
        return True if now() >= self.expiration else False

    class Meta:
        verbose_name = 'EmailVerification'
        verbose_name_plural = 'EmailVerifications'
