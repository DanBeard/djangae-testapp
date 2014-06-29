#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testapp.settings")

    sys.path.insert(0, os.path.join(os.path.dirname(__file__), "lib"))
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), "lib/google_appengine"))

    from djangae.sandbox import activate

    if not "--sandbox" in sys.argv:
        sandbox = "local"
    else:
        sandbox = sys.argv[sys.argv.index("--sandbox") + 1]

    with activate(sandbox):
        from django.core.management import execute_from_command_line
        execute_from_command_line(sys.argv)
