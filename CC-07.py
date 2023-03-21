#!/usr/bin/env python3

# Script: Ops 301 Class 06 Ops Challenge Solution
# Author:Ethan Brock
# Date of latest revision: 21MAR2023
# Purpose: utilizes a function from the os library to generate directory information.

    #REQUIREMENTS
# Create a Python script that generates all directories, sub-directories and files for a user-provided directory path.
    #Script must ask the user for a file path and read a user input string into a variable.
    #Script must use the os.walk() function from the os library.
    #Script must enclose the os.walk() function within a python function that hands it the user input file path.

    #DEMO
# Import libraries

    # import os

# Declaration of variables

### Read user input here into a variable

# Declaration of functions

### Declare a function here
#for (root, dirs, files) in os.walk("testdir"):
#     ### Add a print command here to print ==root==
#    print(root)
#    ### Add a print command here to print ==dirs==
#    print(dirs)
#    ### Add a print command here to print ==files==
#    print(files)

# Main

### Pass the variable into the function here

# End

        # DEMO2
    ## How to define a function

    # def my_function():
    # print("Hello from a function")

    # How to call a function

    # my_function()

    # How to pass arguments into functions

    # def my_function(fname):
    # print(fname + " Refsnes")

    # my_function("Emil")
    # my_function("Tobias")
    # my_function("Linus")

    # How to read input (refer to https://www.w3schools.com/python/python_user_input.asp)

    # username = input("Enter username:")
    # print("Username is: " + username)

    # Start Code
# Import libraries

import os

# Declaration of variables
### Read user input here into a variable
path = input("Please enter a File Path:")
print("You entered: " + path)

# Declaration of functions

def list_info(path):
    for root, dirs, files in os.walk(path):
        print("Root: ", root)
        print("Sub-Directories = ", dirs)
        print("Files = ", files)
        print('-' * 10)


# Call function
list_info(path)
    # End Code