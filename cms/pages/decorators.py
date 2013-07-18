from functools import wraps
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib import messages

from django.core.urlresolvers import reverse

def is_superuser(f):
    @wraps(f)
    def wrapper(request, *args, **kwds):
        if request.user.is_superuser:
            return f(request, *args, **kwds)
        else:
            messages.add_message(request, messages.INFO, 'You are not an admin')
            return HttpResponseRedirect(reverse('page-index'))
    return wrapper
