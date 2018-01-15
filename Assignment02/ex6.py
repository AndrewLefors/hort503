#Assign variable
types_of_people = 10.
#Prints the string and uses variable. Requires f for variable to work
x = f"There are {types_of_people} types of people"

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}"

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny!? {}"
#This line sources the variable hilarious into the variable joke_evaluation
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."
#This line prints the two string variables in order of appearence
print(w + e)
