import string

__author__ = 'patrick'

alphas = string.ascii_letters + '_'
nums = string.digits
overall = alphas+nums

print(alphas)
print(nums)


print('Welcome to the Identifier Checker v1.0')
print('Testees must be at least 2 chars long.')


my_input = input('Identifier to Test:')
print(my_input)

if len(my_input)>1:
    if my_input[0] not in alphas:
        print('''invalid input,
         first symbols must be alphanumberic ''')
    else:
        for otherChar in my_input[1:]:
            if otherChar not in overall:
                print('''invalid:
                remaining symbols must be alphanumberic but %s is not''' % otherChar)
                break
        else:
            print('okay as an identifier')
