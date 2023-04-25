from datetime import timedelta
from uuid import uuid4

from celery import shared_task
from django.utils.timezone import now

from users.models import EmailVerifications, User


@shared_task
def send_email_verification(user_id):
    user = User.objects.get(user=user_id)
    expiration = now() + timedelta(hours=48)
    email_object = EmailVerifications.objects.create(user_id=user_id, code=uuid4(), expiration=expiration)
    email_object.sending_email()
