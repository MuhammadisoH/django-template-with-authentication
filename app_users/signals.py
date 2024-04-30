from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Student

User = get_user_model()


@receiver(signal=pre_save, sender=User)
def change_username_on_email_change(sender, instance, **kwargs):
    user = instance
    index = user.email.index('@')

    if user.email[:index] != user.username:
        user.username = user.email[:index]
        user.save()


@receiver(signal=post_save, sender=User)
def print_after_user_saved(sender, instance, created, **kwargs):
    user = instance

    if created:
        print("[NEW USER]", user, "foydalanuvchisi yaratildi")
    
    else:
        print("[OLD USER]", user, "foydalanuvchisi ma'lumotlari yangilandi")


@receiver(signal=pre_delete, sender=Student)
def print_before_student_delete(sender, instance, **kwargs):
    student = instance
    print("[PRE DELETE]", student, "studenti o'chirilmoqda")


@receiver(signal=post_delete, sender=Student)
def print_after_student_delete(sender, instance, **kwargs):
    student = instance
    print("[POST DELETE]", student, "studenti o'chirilmoqda")
