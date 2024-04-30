from functools import wraps
from django.shortcuts import redirect

def is_superuser(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect("home")

        return func(request, *args, **kwargs)
    return wrapper
