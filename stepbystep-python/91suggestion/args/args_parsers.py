import sys


class ArgParser:
    def __init__(self):
        pass

    @staticmethod
    def parse_args():
        print('Count:', len(sys.argv))
        print('Type:', len(sys.argv))
        print('Content', sys.argv[0])


if __name__ == '__main__':
    ArgParser.parse_args()
