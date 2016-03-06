__author__ = 'patrick'

from collections import MutableMapping


class CaseInsensitiveNamespace(MutableMapping):
    def __init__(self):
        self.ns = {}

    def __getitem__(self, key):
        return self.ns[key.lower()]

    def __delitem__(self, key):
        del self.ns[key.lower()]

    def __setitem__(self, key, value):
        self.ns[key.lower()] = value

    def __len__(self):
        return len(self.ns)

    def __iter__(self):
        return iter(self.ns)
