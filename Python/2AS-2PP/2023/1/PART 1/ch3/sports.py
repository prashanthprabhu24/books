"""
n Python, a dict (short for dictionary) is a collection of things, like lists and
tuples. The difference between dicts and lists or tuples is that each item in a
dict has a key and a corresponding value

If we store information in a dictionary, with the person’s name as
the key and their favorite sport as the value
"""

favorite_sports = {'Ralph Williams': 'Football',
                   'Michael Tippett': 'Basketball',
                   'Edward Elgar': 'Baseball',
                   'Rebecca Clarke': 'Netball',
                   'Ethel Smyth': 'Badminton',
                   'Frank Bridge': 'Rugby'}
print(favorite_sports['Rebecca Clarke'])

# To delete a value in a dict, use its key.
del favorite_sports['Ethel Smyth']
print(favorite_sports)

# To replace a value in a dict, we also use its key.
favorite_sports['Ralph Williams'] = 'Ice Hockey'
print(favorite_sports)
