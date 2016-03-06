import os

__author__ = 'patrick'

def disk():
    """
    getting the disk information
    :return:
    """

    grains={}
    disk=os.statvfs("/")
    print('raw disk information: %s' % str(disk))
    grains['disk']=(disk.f_bsize*disk.f_blocks)/1024/1024/1024
    return grains


if __name__ == '__main__':
    print(disk())
