__author__ = 'patrick'

import sys

if __name__ == '__main__':
    if sys.version_info < (3, 0):
        print("\nThis is the Python 3 version of Python Koans, but you are " +
              "running it with Python 2!\n\n"
              "Did you accidentally use the wrong python script? \nTry:\n\n" +
              "    python3 contemplate_koans.py\n")
    else:
        if sys.version_info < (3, 3):
            print("\n" +
                  "********************************************************\n" +
                  "WARNING:\n" +
                  "This version of Python Koans was designed for " +
                  "Python 3.3 or greater.\n" +
                  "Your version of Python is older, so you may run into " +
                  "problems!\n\n" +
                  "But lets see how far we get...\n" +
                  "********************************************************\n")

        from koans.runner.mountain import Mountain

        Mountain().walk_the_path(sys.argv)