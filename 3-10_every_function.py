languages = ['french', 'english', 'italian', 'portuguese', 'spanish', 'german']

print('Original order of the "languages" list: ')
print(languages)

# append() method
# insert() method
# del statement
# pop() method
# remove() method
# sort() method
# sorted() function
# reverse() method
# len() function


# append() method

languages.append('arabic')

print('appended arabic')
print(languages)

# insert() method

languages.insert(2, 'japanese')

print('inserted japanese at index 2')
print(languages)

# del statement

del languages[3]
print('deleted index 3')
print(languages)

# pop() method

popped_language = languages.pop()
print('popped language ' + popped_language + ', list:')
print(languages)

# remove() method

languages.remove('portuguese')
print('removed portuguese')
print(languages)

# sorted() function

print('temporarily sorted')
print(sorted(languages))
print('language list after sorted()')
print(languages)

# sort() method

languages.sort()

print('after sort()')
print(languages)

# reverse() method

languages.reverse()
print('Order reversed')
print(languages)

# len() function

print('number of languages: ')
print(len(languages))
