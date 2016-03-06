from jinja2 import Environment, PackageLoader

__author__ = 'patrick'

pom_dict = {}
pom_dict['groupId'] = 'io.hedwig.sideprojects'
pom_dict['artifactId'] = 'template'

evn=Environment(loader=PackageLoader('jinjia2_usage','templates'))
evn.get_template('pom_template.xml').stream(pom_dict).dump("pom.xml")
