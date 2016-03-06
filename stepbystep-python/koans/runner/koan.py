import re
import unittest

__author__ = 'patrick'

__all__ = ["__", "___", "____", "_____", "Koan"]
__ = "-=> FILL ME IN! <=-"


class ___(Exception):
    pass


____ = "-=> TRUE OR FALSE? <=-"

_____ = 0


class Koan(unittest.TestCase):
    def assertNoRegexpMatches(self, text, expected_regex, msg=None):
        """
        Throw an exception if the regular expression pattern is not matched
        """
        if isinstance(expected_regex, (str, bytes)):
            expected_regex = re.compile(expected_regex)
        if expected_regex.search(text):
            msg = msg or "Regexp matched"
            msg = '{0}: {1!r} found in {2!r}'.format(msg, expected_regex.pattern, text)
            raise self.failureException(msg)
