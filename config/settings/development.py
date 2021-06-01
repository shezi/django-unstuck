# Django-Unstuck development settings

from .base import *


try:
    from .local import *
except ImportError:
    pass
