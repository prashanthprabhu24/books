"""
 If you really want to use single or double quotes to
surround a string in Python, instead of three single quotes, you can add a
backslash (∖) before each quotation mark within the string. This is called
escaping. It’s a way of telling Python, “Yes, I know I have quotes inside my
string, and I want you to ignore them until you see the end quote.”
"""

single_quote_str = 'He said, "Aren\'t can\'t shouldn\'t wouldn\'t."'
double_quote_str = "He said, \"Aren't can't shouldn't wouldn't.\""
print(single_quote_str)
print(double_quote_str)
