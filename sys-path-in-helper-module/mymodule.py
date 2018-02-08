# Import a module with the same name from a different directory.

import importlib
import os
import sys

if not hasattr(importlib, 'reload'):
    importlib.reload = reload  # for Python 2 compatibility

sys.path.insert(0, os.path.abspath('../module-subdirectory'))
importlib.reload(sys.modules[__name__])

del importlib
del os
del sys

from mymodule import *
