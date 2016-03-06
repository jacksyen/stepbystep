__author__ = 'patrick'

import sys
from os.path import join, dirname
from types import ModuleType

class MagicModule(ModuleType):
    @property
    def git_hash(self):
        fn = join(dirname(__file__),
                  '.git/refs/heads/master')
    with open(fn) as f:
        return f.read().strip()

old_mod = sys.modules[__name__]
sys.modules[__name__] = mod = MagicModule(__name__)
mod.__dict__.update(old_mod.__dict__)