# These three dictionary methods will return list-like values but
# they are not true lists: immutable, do not have append()

spam = {'color': 'red', 'age': 42}

for v in spam.values():
    print(v)

for k in spam.keys():
    print(k)

for i in spam.items(): # dict_items are key-value pairs
    print(i)

# get() method for dictionary arg1 is key of value, arg2 is default value in case it is not there
picnicItems = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')
print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.')
# Without get() we would get a KeyError


spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('color', 'black')
print(spam)

spam.setdefault('color', 'white')
print(spam)

# first time setdefault() is called, dictionary in spam changes
# second time won't change it, because spam already has a key named 'color'

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)

# setdefault() is called to ensure that the key is in the count dictionary (with a default value of 0)
# so that the program doesn't throw KeyError