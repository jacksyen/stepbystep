__author__ = 'patrick'


class JavaProject:
    default_config_dict = {
        'main': 'main/java',
        'test': 'test/java',
        'mainResource': 'main/java/resources',
        'testResources': 'test/java/resources',
        'config': 'config',
        'domain': 'domain',
        'repository': 'repository',
        'rest': {'dto': 'dto', 'controller': 'controller'}
    }

    def __init__(self):
        self.config = self.default_config_dict['config']
        self.domain = self.default_config_dictt['domain']
        self.repository = self.default_config_dict['repository']
        self.rest = self.default_config_dict['rest']
        self.group_id = ''
        self.modules = []
        self.artifact_id = ''
        self.path = ''

    def groupId(self, group_id):
        self.group_id = group_id

    def modules(self, modules):
        self.modules.append(modules)

    def folder_structure(self, config_dict):
        self.config = config_dict['config']
        self.domain = config_dict['domain']
        self.repository = config_dict['repository']
        self.rest = config_dict['rest']

    def path(self, path):
        self.path = path
