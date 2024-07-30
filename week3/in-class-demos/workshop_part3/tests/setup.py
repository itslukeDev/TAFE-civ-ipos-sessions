import sys
import os

# NOTE: Not sure if this is still needed but here is the 'proper' way to insert the path


def insert_pardir():
    module_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.path.pardir)
    )
    if module_path not in sys.path:
        sys.path.insert(0, module_path)
