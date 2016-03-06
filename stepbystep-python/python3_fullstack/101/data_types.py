# Numbers
a_integer = 1234
a_float = 69.89

# Booleans
of_horse = True
nope = False

# Binary
as_bytes = b'A Random text stored as bytes'

# Nothing
my_money = None

# Sequences
a_string = 'Python is Awesome'
a_string_quotes = "Python is Awesome"
a_string_triple = '''Python
                    is
                    Awesome!
                '''

# List,contains any size,any data type
a_list = [1, [2], 1, a_string, 3.67]
print(type(a_list))
# tuple
a_tuple = (5, ['z'], 89,)
a_tuple_comma = 5, ['Z'], 89,
print(type(a_tuple_comma))

# set, no duplicated elements
a_set = set([1, 1, 3, 1])

# Dictionaries
a_dict = {
    'some_key': 'some_value',
    4: 'another value',
    'list': a_list,
    'tuple':a_tuple
}

print(a_dict)

