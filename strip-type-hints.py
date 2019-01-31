import re

from strip_hints import strip_file_to_string
import os
import fnmatch
import sys


def _find_files(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                yield filename


def _strip_hints():
    base_path = os.path.relpath("ascii_canvas")

    for path in _find_files(base_path, "*.py"):
        file_str = strip_file_to_string(
            path,
            to_empty=False,
            no_ast=False,
            no_colon_move=False,
            only_assigns_and_defs=False,
        )

        # remove typing imports
        file_str = re.sub("from typing.*", "", file_str)

        print("temp")
        with open(path, "w") as f:
            f.write(file_str)


_strip_hints()
