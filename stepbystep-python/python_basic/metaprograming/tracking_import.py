import sys
import builtins

__author__ = 'patrick'

real_import = builtins.__import__

print(real_import)


def debug_import(name, locals=None, globals=None, fromlist=None, level=-1):
    glob = globals() or sys._getframe(1).f_globals
    importer_name=glob and glob.get('__name__') or 'unknown'
    print('%s imports %s' % (importer_name,name))
    return real_import(name,locals,globals,fromlist,level)

builtins.__import__=debug_import

def print_frame_info(frame):
    print('module:%s' % frame.f_globals.get('__name__'))
    print('filename:%s' % frame.f_code.co_filename)
    print('current line: %d' % frame.f_lineno)
    loc=dict(k,v) for k,v in frame.f_locals.iteritems() if not k.startswith('__')
    print('local variable: %s' % loc)