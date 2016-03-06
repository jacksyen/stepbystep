# _*_ coding=utf-8 _*_
__author__ = 'patrick'


class HTTPError(Exception):
    def __init__(self, url, err_code, err_msg):
        self.url = url
        self.err_code = err_code
        self.err_msg = err_msg

    def __str__(self):
        return "<HTTPError for %s,%s,%s>" % (self.url, self.err_code, self.err_msg)


try:
    raise HTTPError("http://www.google.com", "404", "NOT FOUND")
except HTTPError:
    print HTTPError("http://www.google.com", "404", "NOT FOUND")
