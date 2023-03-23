#!/usr/bin/env python3

# Script: Ops 301 Class 09 Ops Challenge Solution
# Author:Ethan Brock
# Date of latest revision: 23MAR2023
# Purpose: use "if" statements

    #REQUIREMENTS
# Create if statements using these logical conditionals below. Each statement 
# should print information to the screen depending on if the condition is met.

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

# Create an if statement using a logical conditional of your choice
# and include elif keyword that executes when other conditions are not met.

# Create an if statement that includes both elif and else to execute when both
# if and elif are not met.
    #DEMO
#!/usr/bin/env python3

    # a = 33
    # b = 200
    # if b > a:
    #    print("b is greater than a")

# Be sure to indent while writing an if statement, or else Python will error out.

    # a = 33
    # b = 200
    # if b > a:
    # print("b is greater than a") # you will get an error

# Use elif to add a condition that only checks if previous condition is not met

    # a = 33
    # b = 33
    # if b > a:
    #   print("b is greater than a")
    # elif a == b:
    #   print("a and b are equal")

# Use and to make two conditions

    # a = 200
    # b = 33
    # c = 500
    # if a > b and c > a:
    #   print("Both conditions are True")

# You can nest conditionals within each other

    # if x > 10:
    # print("Above ten,")
    # if x > 20:
    #     print("and also above 20!")
    # else:
    #     print("but not above 20.")

    # Start Code
# get a and b from user input
a = int(input("Enter a value: "))
b = int(input("Enter b value: "))

# Equals: a == b
if a == b:
    print("a is equal to b")

# Not Equals: a != b
if a != b:
    print("a is not equal to b")

# Less than: a < b
if a < b:
    print("a is less than b")

# Less than or equal to: a <= b
if a <= b:
    print("a is less than or equal to b")

# Greater than: a > b
if a > b:
    print("a is greater than b")

# Greater than or equal to: a >= b
if a >= b:
    print("a is greater than or equal to b")

# Create an if statement using a logical conditional of your choice
# and include elif keyword that executes when other conditions are not met.
if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")
else:
    print("a is less than b")

# Create an if statement that includes both elif and else to execute when both
# if and elif are not met.
if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")
else:
    print("a is less than b")
    if b - a >= 8:
        print("The difference between a and b is greater than or equal to 8")
    elif b - a >= 41:
        print("The difference between a and b is greater than or equal to 41")
    else:
        print("The difference between a and b is less than 8")

    # End Code