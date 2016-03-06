import sys
import threading
import traceback
import time

__author__ = 'patrick'


def dump_threads():
    for thread_id, frame in sys._current_frames().items():
        print('Thread #%d' % thread_id)
        print(''.join(traceback.format_stack(frame)))


def foo():
    for x in range(10):
        time.sleep(1)

threading.Thread(target=foo).start()
dump_threads()
