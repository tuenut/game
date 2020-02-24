import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.data.orm.orm.settings")

import django

from django.conf import settings

django.setup()

from app.data.controller import DataController

__all__ = ["DataController"]
