# _*_ coding=utf-8 _*_
__author__ = 'patrick'

class Bank():
    crisis =False
    def create_atm(self):
        while not self.crisis:
            yield "$10.00"

hsbc = Bank()
hsbc_atm=hsbc.create_atm()
"""
iterator
"""
print hsbc_atm.next()

print ([hsbc_atm.next() for cash in range(5)])

hsbc.crisis=True
print hsbc_atm.next()