#Import mean function from statistics module
from statistics import mean
fav_num = float(input('What is your favorite number?' ))
#This line is useless as it does not define int(fav_num)
#int(fav_num)
#fav_num = float(fav_num)
print(fav_num)

not_a_number = float(input('This is still a number to pick! ')
print(not_a_number)

not_fav = float(input('What is your least favorite number?'))
#This line would work, however float does similar function
# not_fav = int(not_fav)
#Do not need this line if float is above
#not_fav = float(not_fav)
print(not_fav)

random_num = float(input('Now pick a random number.' ))
#int(random_num)
#random_num = float(random_num)
print(random_num)

one_to_ten_number = float(input('Choose a value between 1-10 '))
#int(one_to_ten_number)
#one_to_ten_number = float(one_to_ten_number)
print(one_to_ten_number)

another_number = float(input('Pick another number! '))
#int(another_number)
#another_number = float(another_number)
print(another_number)

more_numbers = float(input('Pick More Numbers! '))
#more_numbers = float(more_numbers)
print(more_numbers)

even_more_num = float(input('We need even more numbers! '))
#even_more_num = float(even_more_num)
print(even_more_num)

only_two_more = float(input('Only two more numbers to pick! '))
#only_two_more = float(only_two_more)
print(only_two_more)

one_more_num = float(input('You have one more number to pick after this! ')
print(one_more_num)


last_num = float(input('This is the last number.' )
print(last_num)

average = mean([fav_num, not_fav, random_num, one_to_ten_number, another_number, more_numbers, even_more_num, only_two_more, one_more_num, last_num])
print(f"The average of your values is {average}.")
