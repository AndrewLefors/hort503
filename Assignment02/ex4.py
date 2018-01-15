#This line assigns the variable cars
cars = 100.
#This line assigns the variable space_in_a_car
space_in_a_car = 4.
#This line assigns the variable drivers
drivers = 30.
#This line assigns the variable passengers
passengers = 90.
#This line assigns the variable cars_not_driven as the difference between two variables
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "people today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
