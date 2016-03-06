# _*_ coding=utf-8 _*_
import os
import shutil
import sys

__author__ = 'patrick'

def version_file(file_spec,vtype='copy'):
    if os.path.isfile(file_spec):
        if vtype not in ('copy','rename'):
            raise ValueError,'Unknow vtyp'+vtype
        n,e=os.path.splitext(file_spec)
        print n,e,file_spec
        if len(e)==4 and e[1:].isdigit():
            num=1+int(e[1:])
            root=n
        else:
            num=0
            root=file_spec

        for i in xrange(num,1000):
            new_file='%s.%03d' %(root,i)
            if not os.path.exists(new_file):
                if vtype=='copy':
                    shutil.copy(file_spec,new_file)
                else:
                    os.rename(file_spec,new_file)
                return vtype+'success!'
        raise RuntimeError,"can't %s%r,all names take"%(vtype,file_spec)
    return vtype+'failed!'

if __name__ == '__main__':
    print sys.argv
    if len(sys.argv)==2:
        print version_file(sys.argv[1])
    else:
        print 'error! usage:./bak.py file'
        sys.exit(1)