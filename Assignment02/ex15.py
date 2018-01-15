#Import argv from system
from sys import argv
#assign script as first variable of argv and filename as second variable
script, filename = argv
#This line opens a text file
txt = open(filename)
close({txt})
#This line prints the name of your file
print(f"Here's your file {filename}:")
#This line prints the contents of the file to standard output
print(txt.read())
close(filename)
#This line prompts the user for the file name
print("Type the filename again:")
file_again = input("> ")
#This line assigns the txt_again variable to the opening the assoicated file
txt_again = open(file_again)
#This line prints the contents of the file associated with the variable
print(txt_again.read())
close({txt_again})
