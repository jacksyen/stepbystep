__author__ = 'simon'

import os

print os.listdir("/home/simon/tools")

for root,dirs,files in os.walk("/home/simon/tools"):
    print root,dirs,files

