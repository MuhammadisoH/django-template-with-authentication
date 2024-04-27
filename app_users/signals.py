from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

User = get_user_model()


@receiver(signal=pre_save, sender=User)
def print_user(sender, instance, **kwargs):
    user = instance
    index = user.email.index('@')

    if user.email[:index] != user.username:
        user.username = user.email[:index]
        user.save()
