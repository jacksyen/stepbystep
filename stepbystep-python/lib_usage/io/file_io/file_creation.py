# _*_ coding=utf-8 _*_
__author__ = 'patrick'


def create_file(line):
    f = open('test.txt', 'w')
    f.writelines(line)


def write_dict(file_lists):
    config= read_properties()
    notes={}
    notes['rr_id']=config['rr_id']
    notes['summary']=config['summary']+'summary revised'
    notes['description']=config['description']
    notes['target_user']=config['target_user']
    print type(file_lists)
    try:
        original_file = config['file_lists'].split(',')
        print type(original_file)
        original_file.extend(file_lists)
        print original_file
    except KeyError :
        original_file=[]

    original_file = list(set(original_file+file_lists))
    notes['file_lists']=','.join(original_file)

    with open('notes.txt','w') as f:
        for k in notes:
            f.write('%s="%s"'%(k,notes[k]))
            f.write('\n')

    print config

def read_properties():
    config={}
    with open('notes.txt') as f:
        exec (compile(f.read(), 'notes.txt', 'exec'), config)
    return config

if __name__ == '__main__':
    write_dict(['123','444','00989','555674','0090098765'])