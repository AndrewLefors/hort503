from statistics import mean
fav_num = float(input('What is your favorite number?\n' ))
#This line is useless as it does not define int(fav_num)
#int(fav_num)
#fav_num = float(fav_num)
print(fav_num)

not_a_number = float(input('This is still a number to pick!\n' ))
print(not_a_number)

not_fav = float(input('What is your least favorite number?\n' ))
#This line would work, however float does similar function


print(not_fav)

random_num = float(input('Now pick a random number.\n' ))

#random_num = float(random_num)
print(random_num)

one_to_ten_number = float(input('Choose a value between 1-10 \n' ))

print(one_to_ten_number)

another_number = float(input('Pick another number!\n' ))

print(another_number)

more_numbers = float(input('Pick More Numbers!\n' ))

print(more_numbers)

even_more_num = float(input('We need even more numbers!\n' ))

print(even_more_num)

only_two_more = float(input('Only two more numbers to pick!\n' ))

print(only_two_more)

one_more_num = float(input('You have one more number to pick after this!\n' ))
print(one_more_num)


last_num = float(input('This is the last number.\n' ))
print(last_num)

average = mean([not_a_number, fav_num, not_fav, random_num, one_to_ten_number, another_number, more_numbers, even_more_num, only_two_more, one_more_num, last_num])
print(f"The average of your values is {average}.")
