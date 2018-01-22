#Makes a function to perform the print task below, but only prints when
#The function is called.
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I got Nothin\'.")
#These lines call the functions defined above, and provides the
#argument values within the (""). 
print_two("Andrew", "Lefors")
print_two_again("Andrew", "Lefors")
print_one("First!")
print_none()
