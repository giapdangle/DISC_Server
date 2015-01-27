#!/usr/bin/env python
import os
import sys
os.environ.setdefault('LANG','en_US') #fix to prevent errors from null locale

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangosite.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)