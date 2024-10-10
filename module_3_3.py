def print_params(a=1, b='string', c=True):
    print(a, b, c)


values_list = [2, 'строка', False]
values_dikt = {'a':1 ,'b':'string', 'c':False}
values_list_2 = [3, True]

print_params(b = 25)
print_params(c = [1,2,3])
print_params()
print_params(*values_list)
print_params(**values_dikt)
print_params(*values_list_2, 42)