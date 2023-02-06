"""
Suppose you are digging in your backyard and uncover a bag of 20 gold
coins. The next day, you sneak down to the basement and stick the coins
inside your grandfather’s steam-powered replicating invention (luckily, you
can just fit the 20 coins inside). You hear a whiz and a pop and, a few hours
later, out shoot another 10 gleaming coins.
Now, what if a raven spots the shiny gold sitting in your bedroom, and
every week flies in and manages to steal three coins? How many coins
would you have left at the end of the year?
"""

found_coins = 20
magic_coins = 10
stolen_coins = 3
print(found_coins + magic_coins * 365 - stolen_coins * 52)

# What if you stick a scarecrow in your
# window, and the raven steals only two coins instead of three?What if you stick a scarecrow in your
# window, and the raven steals only two coins instead of three?
stolen_coins = 2
print(found_coins + magic_coins * 365 - stolen_coins * 52)

# if you bang the sides of your grandfather’s invention at the right moment, and it spits out three extra coins each
# time, if you bang the sides of your grandfather’s invention at the right moment, and it spits out three extra coins
# each time,
magic_coins = 13
print(found_coins + magic_coins * 365 - stolen_coins * 52)
