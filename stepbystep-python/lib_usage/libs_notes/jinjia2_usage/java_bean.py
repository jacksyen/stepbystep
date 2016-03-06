import json

__author__ = 'patrick'


class JavaBean:
    def __init__(self):
        self.members = []
        self.entity_name = 'GeneratedClass'

    # def __init__(self, class_name):
    #     self.members = []
    #     self.class_name = class_name
    #
    # def __init__(self, class_name, members):
    #     if type(members) is list:
    #         raise Exception('members should be a list')
    #     self.members = members
    #     self.class_name = class_name

    def member(self, name, var_type='String'):
        member_des = {'name': name, 'type': var_type}
        self.members.append(member_des)
        return self

    def name_class(self, entity_name):
        self.entity_name = entity_name
        return self

    def to_json(self):
        d = {'__classname__': type(self).__name__}
        d.update(vars(self))
        return d
