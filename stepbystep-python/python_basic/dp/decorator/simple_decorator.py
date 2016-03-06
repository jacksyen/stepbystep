__author__ = 'patrick'


def greet(name):
    return 'Hello ' + name


greet_some = greet

print(greet_some("patrick"))


def greet_new(name):
    def get_message():
        return 'Hello '

    result = get_message() + name
    return result


print(greet_new("simon"))


# pass function
def call_func(func):
    other_name = "john"
    return func(other_name)


print(call_func(greet))


# return function
def compose_func():
    def get_message():
        return "Hello There!"

    return get_message


func_1 = compose_func();
print(func_1())


# decorator constructor
def get_text(name):
    return "this is {0} shit".format(name)


def p_decorator(func):
    def func_wrapper(name):
        return "<p>{0}<p>".format(func(name))

    return func_wrapper

my_get_text=p_decorator(get_text)
print(my_get_text("SIMON"))

# annotation like
@p_decorator
def hello_world(name):
    return "Hello {0} World".format(name)

print(hello_world("Su Su"))

