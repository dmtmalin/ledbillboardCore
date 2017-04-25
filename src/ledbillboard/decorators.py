# -*- coding: utf-8 -*-
from django.core.exceptions import PermissionDenied
from django.utils.decorators import available_attrs
from django.utils.six import wraps


def login_required_forbidden(view_func):
    @wraps(view_func, assigned=available_attrs(view_func))
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated():
            return view_func(request, *args, **kwargs)
        raise PermissionDenied
    return _wrapped_view
