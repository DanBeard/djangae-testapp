#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testapp.settings")

    from fix_path import fix_path
    fix_path()

    from djangae.sandbox import activate

    if "--sandbox" in sys.argv:
        sandbox_arg_index = sys.argv.index("--sandbox")
        sandbox = sys.argv[sandbox_arg_index + 1]
        del sys.argv[sandbox_arg_index + 1]
        del sys.argv[sandbox_arg_index]
    else:
        sandbox = "local"

    with activate(sandbox):
        from django.core.management import execute_from_command_line
        execute_from_command_line(sys.argv)
