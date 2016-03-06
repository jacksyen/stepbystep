import random


def telling_truth():
    print('Telling truth')


def function_with_params(params):
    print(params)


def comments_in_functions():
    """
    this is comments in functions
    :return:
    """
    print("comments")


def this_year():
    return 2016


lambda_function=lambda param:param*param
print(lambda_function(10))


email = "test"+str(random.randint(0,1000))+"@flask.com"
print(email)
add_date = """
    {"test":{user_email}
    "type": "users"}}
    """
print(add_date)

