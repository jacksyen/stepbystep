import ast

__author__ = 'patrick'
## AST Hack

x = ast.parse('1+2',mode='eval');
x.body.op=ast.Sub()
print(eval(compile(x,'<string>','eval')))