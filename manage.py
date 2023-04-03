#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import re
import sys
from django.core.cache import cache

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Manual_review.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    l = os.listdir(r'F:\toolkit\workspace\glb')
    for f in l:
        if not f.endswith('.glb'):
            hex_uid = re.search(r'([a-f|0-9]+)_render', f).group(1)
            cache.set(hex_uid, f)
    main()
