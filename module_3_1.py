calls = 0
def count_cals():
    global calls
    calls+=1


def string_info (string):
    count_cals()
    return (len(string), string.upper() ,string.lower())


def is_contains (string, list_to_search):
    count_cals()
    return (string.upper()in [s.upper() for s in list_to_search])


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)




