# _*_ coding=utf-8 _*_
__author__ = 'patrick'

def attributesFromDict(self,d):
	self = d.pop('self')
	for n,v in d.itemritems():
		setattr(self,n,v)
'''
	__init__方法里千遍一律的赋值语句大概是这个样子的:
	def __init__(self,foo,bar,baz,boom=1,bang=2):
		self.foo = foo
		self.bar = bar
		self.baz = baz
		self.boom = boom
		self.bang = bang

	#########################################################

	现在可以被缩减为清晰的一行:
	def __init__(self,foo,bar,baz,boom=1,bang=2):
		attributesFromDict(locals())
'''

class AutoInit():
    def __init__(self,foo,bar):
        print locals()
        attributesFromDict(locals())

a = AutoInit("123","223")
