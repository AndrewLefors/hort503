tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a {}."
backslash_cat = "{} \\ {} \\ {}."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print(tabby_cat)
print(persian_cat.format('line'))
print(backslash_cat.format("I'm", "a", "cat"))
print(fat_cat)
