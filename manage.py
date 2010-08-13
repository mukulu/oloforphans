#!/usr/bin/env python
""" Management of the entire oloforphans webiste and its appplications
That includes database management, development testing, and shell client
with pre-configred settings.
"""
from django.core.management import execute_manager
try:
    import settings # Assumed to be in the same directory.
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r.\nPlease create a settings.py file from settings.py.sample adjusting it to your database settings.\nOr you'll have to run django-admin.py, passing it settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow. check it out.)\n" % __file__)
    sys.exit(1)

if __name__ == "__main__":
    execute_manager(settings)
