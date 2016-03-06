__author__ = 'patrick'

import sys


def caller_line_no():
    return sys._getframe(1).f_lineno


def caller_filename():
    return sys._getframe(1).f_code.co_filename


def implements(*interfaces):
    cls_scope = sys._getframe(1).f_locals
    metacls = cls_scope.get('__metaclass__')
    new_metacls = magic_metaclass_factory(interfaces, metacls)
    cls_scope['__metaclass__'] = new_metacls


def find_request():
    frm = sys._getframe(1)
    while frm is not None:
        if 'request' in frm.f_locals and \
                hasattr(frm.f_locals['request'], 'META'):
            return frm.f_locals['request']
        frm = frm.f_back
