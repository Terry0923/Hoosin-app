from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
import re

# USER_FIELDS = ['username', 'email']
#
# def allowed_email(email):
#     return re.match('.*@virginia\.com', email)
#
# def create_user(strategy, details, backend, user=None, *args, **kwargs):
#
#     if allowed_email():
#         messages.success(request, f'Your account has been created! You are now able to log in')
#         return redirect('login')
#     else:
#         return redirect('error')

USER_FIELDS = ['username', 'email']


def allowed_email(email):
    return re.match('.*@acme\.com', email) or \
        re.match('.*@acme\.net', email)


def create_user(strategy, details, backend, user=None, *args, **kwargs):
    if user:
        return {'is_new': False}

    fields = dict((name, kwargs.get(name, details.get(name)))
                  for name in backend.setting('USER_FIELDS', USER_FIELDS))

    if not fields:
        return

    if not allowed_email(fields['email']):
        return

    return {
        'is_new': True,
        'user': strategy.create_user(**fields)
    }
