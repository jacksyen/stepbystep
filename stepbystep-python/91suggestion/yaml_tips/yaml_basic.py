# -*- coding: utf-8 -*-

"""
Load YAML:
    1. list
    2. dict

"""
import os

import yaml


def load_list():
    content = """
        - config
        - domain
        - repository
    """
    return yaml.load(content)


def load_dict():
    content = """
        hello1: test
        hello2: test2
    """
    return yaml.load(content)


def load_all_dict():
    contents = """
      hero:
        hp: 34
        sp: 8
        level: 4
      orc:
        hp: 12
        sp: 0
        level: 2
    """
    return yaml.load(contents)


print(load_list())
print(load_dict())
print(load_all_dict())


def load_with_type():
    contents = """
        none: [~,null]
        bool: [true,false,on,off]
        int: 42
        float: 3.1415
        list: [test1,test2,test3]
        dict: {name: simon,sp: 5}
    """

    return yaml.load(contents)


print(load_with_type())

"""
 Python classes constructed by !!python/object tag
"""


class Hero:
    def __init__(self, name, hp, sp):
        self.name = name
        self.hp = hp
        self.sp = sp

    def __repr__(self):
        return "%s(name=%r,hp=%r,sp=%r)" % (
            self.__class__.__name__, self.name, self.hp, self.sp)


def load_to_instance():
    contents = """
            !!python/object:__main__.Hero
            name: Hero
            hp: 1200
            sp: 0
        """
    return yaml.load(contents)


print(load_to_instance())


def dump_file():
    contents = {
        'name': 'test',
        'first_name': 'simon',
        'last_name': 'kevin'
    }
    # return yaml.dump(contents)
    with open('document.yaml', 'w') as f:
        return yaml.dump(contents, f, default_flow_style=False, default_style='"')


def dump_instance():
    hero = Hero('test', 34, 45)
    with open('hero.yaml', 'w') as f:
        return yaml.dump(hero, f, default_flow_style=False)


def read_yaml_file(yaml_path=None):
    if yaml_path is None:
        yaml_path = 'springboot-folders.yml'
    with open(yaml_path, 'r') as f:
        result = yaml.load(f)

    return result


def get_folders():
    """
    get Folder list according to the yaml file
    :return:
    """
    folders_dict = read_yaml_file()
    template_folders = {}

    for root_folder in folders_dict:
        template_folders[root_folder] = []
        current_node = folders_dict[root_folder]
        if isinstance(current_node, list) or isinstance(current_node, dict):
            template_folders[root_folder].extend(get_folder_list(current_node))
        else:
            template_folders[root_folder].extend(current_node)

    return template_folders


def get_folder_list(configurations, parent_folder=None):
    """
    get Folder list according to the configuration
    :param configurations:
    :param parent_folder:
    :return:
    """
    result = []
    if isinstance(configurations, list):
        for item in configurations:
            result.extend(get_folder_list(item, parent_folder))
    elif isinstance(configurations, dict):
        for item in configurations:
            result.extend(get_folder_list(configurations[item], item))
    else:
        if parent_folder is None:
            result.append(configurations)
        else:
            result.append(parent_folder + '/' + configurations)
    return result


print(dump_file())
print(dump_instance())
folders = read_yaml_file()
print(folders['main'])
print(folders['test'])
print(folders['resources'])
print(get_folders())
