from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
import re


USER_FIELDS = ['username', 'email']


def allowed_email(email):
    return re.match('.*@virginia\.edu', email)


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
