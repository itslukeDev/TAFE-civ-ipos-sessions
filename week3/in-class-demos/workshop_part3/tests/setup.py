import sys
import os


def setup_path():
    module_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.path.pardir)
    )
    sys.path.insert(0, module_path)
