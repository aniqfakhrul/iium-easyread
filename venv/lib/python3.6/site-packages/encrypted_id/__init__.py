# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

try:
    basestring
except NameError:
    basestring = str

from cryptography.fernet import Fernet, InvalidToken

import base64
import hashlib

from django.conf import settings
from django.db.models import Model
from django.http import Http404
from django.shortcuts import get_object_or_404 as go4


__version__ = "1.1.0"
__license__ = "BSD"
__author__ = "Sean Meyer"
__email__ = "slinkymabyday@gmail.com"
__url__ = "https://github.com/slinkymanbyday/django-encrypted-id-cryptography"
__source__ = "https://github.com/slinkymanbyday/django-encrypted-id-cryptography"
__docformat__ = "html"


class EncryptedIDDecodeError(Exception):
    def __init__(self, msg="Failed to decrypt, invalid input."):
        super(EncryptedIDDecodeError, self).__init__(msg)


def encode(the_id):
    assert 0 <= the_id < 2 ** 64
    the_id = str(the_id).encode()
    f = Fernet(settings.ID_ENCRYPT_KEY)
    return f.encrypt(the_id).decode()


def decode(e):
    if e is None:
        raise ValueError()
    if isinstance(e, basestring):
        e = bytes(e.encode("ascii"))

    for skey in getattr(settings, "ID_ENCRYPT_KEYS", [settings.ID_ENCRYPT_KEY]):
        try:
            f = Fernet(skey)
            the_id = f.decrypt(e)
            return int(the_id)
        except ValueError:
            raise EncryptedIDDecodeError("Failed to decrypt, invalid input.")
        except InvalidToken:
            raise EncryptedIDDecodeError("Failed to decrypt, bad decryption key.")

    raise EncryptedIDDecodeError("Failed to decrypt.")


def get_object_or_404(m, ekey, *arg, **kw):
    try:
        pk = decode(ekey)
    except (EncryptedIDDecodeError, ValueError):
        raise Http404

    return go4(m, id=pk, *arg, **kw)


def ekey(instance):
    assert isinstance(instance, Model)
    return encode(instance.pk)
