__author__ = 'patrick'

def mem():
    grains={}
    # MAC doesn't work
    with open('/proc/meminfo') as f:
        lines=f.readlines()

    num = lines[0].strip('\n').split(':')[1]
    total=int(num.split()[0])/1024
    grains['mem']=total
    return grains

if __name__ == '__main__':
    print(mem())
