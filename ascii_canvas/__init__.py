"""Stripping the python 3.6 type hints for backwards compatibility."""
import os
import sys


if sys.version_info.major < 3 or (sys.version_info.major == 3 and sys.version_info.minor < 6):
    from strip_hints import strip_on_import
    strip_on_import(__file__, to_empty=False, no_ast=False, no_colon_move=False,
                    only_assigns_and_defs=False, py3_also=True)
 
