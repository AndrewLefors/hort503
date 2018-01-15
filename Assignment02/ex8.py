#Assign variable to string of variable input
formatter = "{} {} {} {}"
#These lines use the format function for the variable formatter to change the string output
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "I like",
    "Green Bean Casserole",
    "Especially with Gravy",
    "It Reminds Me of Home",
))
