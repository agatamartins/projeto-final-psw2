from functools import wraps

from django.contrib import messages
from django.shortcuts import redirect


def permission_denied_message(permission):
    def decorator(view_func):
        @wraps(view_func)
        def wrapped(request, *args, **kwargs):
            if request.user.is_authenticated and not request.user.has_perm(permission):
                messages.error(
                    request,
                    'Você não tem permissão para executar esta ação.',
                )
                return redirect('inicio')
            return view_func(request, *args, **kwargs)

        return wrapped

    return decorator
