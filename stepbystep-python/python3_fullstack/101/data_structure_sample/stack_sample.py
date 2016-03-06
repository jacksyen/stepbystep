import re


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def isEmpty(self):
        return self.items == []


## stack used to handle a expression

stack = Stack()
stack.push(1)
stack.push(2)
stack.push('+')


def eval_postfix(expression):
    token_list = re.split("([^0-9])", expression)
    stack = Stack()
    for token in token_list:
        if token == '' or token == ' ':
            continue
        if token == '+':
            result = stack.pop() + stack.pop()
            stack.push(result)
        elif token == '*':
            product = stack.pop() * stack.pop()
            stack.push(product)
        else:
            stack.push(int(token))
    return stack.pop()

print(eval_postfix("56 34 + 2 *"))