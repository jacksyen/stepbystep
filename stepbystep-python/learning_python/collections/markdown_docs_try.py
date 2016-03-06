# _*_ coding=utf-8 _*_
import pydoc

__author__ = 'patrick'

class MarkDownDoc():
    """
     # Markdown Doc sample to output Python Doc as Markdown
    """
    def test_mark(self):
        """
        ## Test MarkDown
        """

if __name__ == '__main__':
   doc= MarkDownDoc.__doc__
   all_doc=help(MarkDownDoc)
   temp = dir(MarkDownDoc)[2]
   print help(dir)
   print doc
