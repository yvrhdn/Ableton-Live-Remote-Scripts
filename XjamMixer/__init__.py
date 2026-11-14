from __future__ import absolute_import, unicode_literals
from .XjamMixer import XjamMixer


def create_instance(c_instance):
    return XjamMixer(c_instance)
