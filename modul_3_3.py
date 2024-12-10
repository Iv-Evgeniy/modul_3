def print_params(a = 1, b = 'string', c = True):
    print(a, b, c)

print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = ('str', 7, False)
values_dict = {'a': 22.5, 'b': 11, 'c': 'one' }
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ('two', 2)
print_params(*values_list_2, 42)