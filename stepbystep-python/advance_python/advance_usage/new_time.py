from datetime import datetime
from urllib.parse import urlparse

__author__ = 'patrick'

print('It\'s {0:%H:%M}'.format(datetime.today()))

url = urlparse('http://pocoo.org/')
print('{0.netloc} [{0.scheme}]'.format(url))
