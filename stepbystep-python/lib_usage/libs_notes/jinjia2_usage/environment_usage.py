from jinja2 import Environment, PackageLoader

__author__ = 'patrick'

env = Environment(loader=PackageLoader('jinjia2_usage', 'templates'))

template = env.get_template('template.txt')
print(template.render(name='test'))

expr = env.compile_expression('foo==42')
print(expr(foo=23))

print(env.compile_expression('var')() is None)
print(env.compile_expression('var', undefined_to_none=False)())