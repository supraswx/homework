def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(1, 2, 4)
print_params(b = 10)
print_params(c = [1, 2, 3])

values_list = [100, False, 'string']
values_dict = {'a': 1, 'b': 'string', 'c': False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['supra', 52]
print_params(*values_list_2, 'нет')