#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testapp.settings")

    from fix_path import fix_path
    fix_path()

    from djangae.sandbox import activate

    if not "--sandbox" in sys.argv:
        sandbox = "local"
    else:
        sandbox = sys.argv[sys.argv.index("--sandbox") + 1]

    with activate(sandbox):
        from django.core.management import execute_from_command_line
        execute_from_command_line(sys.argv)
