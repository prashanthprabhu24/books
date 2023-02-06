"""
Lists.
"""

# We could store this list of items in the wizard_list variable by using a string like so:
wizard_list = 'spider legs, toe of frog, bat wing, slug butter, snake dandruff'
print(wizard_list)

# But we could also create a list, a somewhat magical Python object that we can manipulate
wizard_list = ['spider legs', 'toe of frog', 'bat wing', 'slug butter', 'snake dandruff']
print(wizard_list)

# We can print an item in the list by entering a number (called
# the index position) inside square brackets
print(wizard_list[2])

# We can also change an item in a list
wizard_list[2] = 'snail tongue'
print(wizard_list)

# We can also show a sublist of the items in the list. We do this by using a
# colon (:) inside square brackets. For example, enter the following to see the
# third to fifth items in our list (a brilliant set of ingredients for a lovely
# sandwich):
print(wizard_list[2:5])

# To add items to the end of a list, we use the append function.
wizard_list.append('bear burp')
print(wizard_list)

# You can keep adding more magical items to the wizard’s list in the same
# way
wizard_list.append('mandrake')
wizard_list.append('hemlock')
wizard_list.append('swamp gas')
print(wizard_list)

# To remove items from a list, use the del command (short for delete)
del wizard_list[4]
print(wizard_list)

# Try removing the items we just added (mandrake, hemlock, and swamp
# gas)
del wizard_list[7]
del wizard_list[6]
del wizard_list[5]
print(wizard_list)
