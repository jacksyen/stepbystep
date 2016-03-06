import ast

__author__ = 'patrick'

t =ast.parse('a=1+2')
code =compile(t,'<string>','exec')