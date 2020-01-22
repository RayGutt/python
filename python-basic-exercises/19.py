def add_is(string):
    if string.startswith('Is'):
        return string
    else:
        return 'Is' + string


print(add_is('coucou'))
print(add_is('Isd'))
