from .base import *
from .base import env


SECRET_KEY = env("DJANGO_SECRET_KEY")

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["supplementame.eu"])

DEBUG = False

try:
    from .local import *
except ImportError:
    pass
