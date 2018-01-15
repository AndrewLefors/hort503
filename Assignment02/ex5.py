name = 'Andrew J. Lefors'
age = 23.
height = 74. #inches and that is my height too!
weight = 160. #lbs
eyes = 'Hazel'
teeth = 'White'
hair = 'Brown'
SIweight = weight * 0.453592
SIheight = height * 2.54
print(f"Let's talk about {name}.")
print(f"He's {height} inches tall or {SIheight} centimeters.")
print(f"He's {weight} pounds or {SIweight} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

#This line is tricky, try to get it exactly right. ##Oh I will
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
