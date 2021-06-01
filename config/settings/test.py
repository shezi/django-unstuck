# Django-Unstuck test settings

from .base import *


try:
    from .local import *
except ImportError:
    pass
