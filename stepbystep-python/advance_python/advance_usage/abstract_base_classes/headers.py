from _collections_abc import Mapping

__author__ = 'patrick'


class Headers(Mapping):
    def __init__(self, headers):
        self._headers = headers;

    def __getitem__(self, item):
        ikey = item.lower()
        for key, value in self._headers:
            if key.lower() == ikey:
                return value
            raise KeyError(key)

    def __len__(self):
        return len(self.headers)

    def __iter__(self):
        return (key for key, value in self._headers)


headers = Headers(['Content-Type', 'text/html'])
print(headers['Content-Type'])
