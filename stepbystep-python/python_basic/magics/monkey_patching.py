__author__ = 'patrick'

from a_horrible_library import SomeClass

original_init = SomeClass.__init__


def new__init__(self, *args, **kwargs):
    original__init__(self, *args, **kwargs)
    self.something_else = Thing()


SomeClass.__init__ = new__init__


de = Translations.load(['de_DE', 'de', 'en'])

import __builtin__
__builtin__._ = de.ugettext
__builtin__.__import__ = my_fancy_import