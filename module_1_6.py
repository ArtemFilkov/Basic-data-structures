my_dict = {'Roman':1990,'Igor':1978,'Nikita':1995}
print(my_dict)
print(my_dict['Igor'])
print(my_dict.get('Artem'))
my_dict.update({'Artem':1987,'Oleg':1956})
print(my_dict)
meaning = my_dict.pop('Oleg')
print(my_dict)
print(meaning)
my_set = {2,7,6,5,2,4,7,4,3,'Oleg',True,2.5,'Oleg',2.5}
print(my_set)
my_set = {2,7,6,5,2,4,7,4,3,'Oleg',True,2.5,'Oleg',2.5,9,8}
print(my_set)
print(my_set.discard('Oleg'))
print(my_set)
