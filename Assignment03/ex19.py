#This line creats a function that prints the value of cheese and crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
  print(f"You have {cheese_count} cheeses!")
  print(f"You have {boxes_of_crackers} boxes of crackers!")
  print("Man that's enough for a party!")
  print("Get a blanket. \n")

#This line prints the below string and calls the function
#While giving the integer input
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

#This line prints the string and then assigns two variables fo the
#Amount of cheese and crackers, then calls the function
print("OR we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)
#This line prints the below string and calls the function, while
#Giving a mathmatical input
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


#This line prints the stirng and calls the function, using both the
#Variables and direct input for final number
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def pickles_in_a_jar(Number_of_Pickles):
    Number_of_Pickles = float(input("How many pickles have you eaten today?" ))
    print(f"There are {Number_of_Pickles} in the pickle jar.")
    print("That's not nearly enough pickles.")
    new_num_pickles = Number_of_Pickles + 30
    print(f"The ideal number of pickles is {new_num_pickles}.")
    difference_pickle = new_num_pickles - Number_of_Pickles
    print(f"You need {difference_pickle} more pickles.")
pickles_in_a_jar
