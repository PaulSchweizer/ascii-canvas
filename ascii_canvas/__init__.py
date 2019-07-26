"""Stripping the python 3.6 type hints for backwards compatibility."""
import os
import sys


if sys.version_info.major < 3 or sys.version_info.minor < 6:

    from strip_hints import strip_hints_main, import_hooks

    item_path = os.path.join(os.path.dirname(__file__), 'item.py')
    canvas_path = os.path.join(os.path.dirname(__file__), 'canvas.py')

    importer = import_hooks.StripHintsImporter()
    stripper = strip_hints_main.HintStripper(
        to_empty=False, no_ast=False,
        no_colon_move=False, only_assigns_and_defs=False)
    module_dir = os.path.dirname(os.path.realpath(item_path))
    importer.stripper_fun_to_use[module_dir] = stripper.strip_type_hints_from_file

    importer.module_info = (None, item_path, None)
    item = importer.load_module(item_path)

    importer.module_info = (None, canvas_path, None)
    canvas = importer.load_module(canvas_path)
