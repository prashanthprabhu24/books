"""
If you want to display a message using the contents of a variable, you can
embed it in a special string, called an f-string (also known as a formatted
string literal). You put braces around the variable name, which will then be
replaced by the actual value. (Embedding values, also referred to as string
substitution, is programmer-speak for “inserting values.”).
"""

myscore = 1000
message = f'I scored {myscore} points'
print(message)

# We can also use more than one variable in a string:
first = 0
second = 8
print(f'What did the number {first} say to the number {second}? Nice belt!!')

print(f'Two plus two equals {2 + 2}')

