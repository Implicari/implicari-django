#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    django_settings_module = os.environ.get('DJANGO_SETTINGS_MODULE', 'config.settings')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', django_settings_module)

    try:
        from django.core.management import execute_from_command_line

    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    execute_from_command_line(sys.argv)
