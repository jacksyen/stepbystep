import sys
from DictionaryServices import *


def main():
    try:
        search_word = sys.argv[1].decode('utf-8')
    except IndexError:
        err_msg = 'You did not enter any term to look up'
        print
        err_msg
        sys.exit()

    word_range = (0, len(search_word))
    dict_result = DCSCopyTextDefintion(None, search_word, word_range)
    if not dict_result:
        err_msg = "'%s' not found in Dictionary." % (search_word)
        print
        err_msg.encode('utf-8')
    else:
        print
        dict_result.encode('utf-8')


if __main__ == '__main__':
    main()
