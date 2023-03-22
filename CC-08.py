#!/usr/bin/env python3

# Script: Ops 301 Class 08 Ops Challenge Solution
# Author:Ethan Brock
# Date of latest revision: 22MAR2023
# Purpose: Work with lists in python

    #REQUIREMENTS
# Create a Python script that includes the following:

# Assign to a variable a list of ten string elements.
# Print the fourth element of the list.
# Print the sixth through tenth element of the list.
# Change the value of the seventh element to “onion”.

    #DEMO

# How to create and print a list

    # thislist = ["apple", "banana", "cherry"]
    # print(thislist)

# How to print the first item only

    # thislist = ["apple", "banana", "cherry"]
    # print(thislist[0])

# How to print the last item only by counting backwards

    # thislist = ["apple", "banana", "cherry"]
    # print(thislist[-1])

# How to print a range of elements in a list

    # thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    # print(thislist[2:5])

# How to print the beginning to a specific element number

    # thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    # print(thislist[:4])

# How to add an item to a list

    # thislist = ["apple", "banana", "cherry"]
    # thislist.append("orange")
    # print(thislist)

    # Start Code

print("List:")
# create list
animals = ["Dog", "Chicken", "Duck", "Turkey", "Wolf", "Coyote", "Racoon", "Opossum", "Horse", "Armadillo"]

print(animals)
# Print the fourth element of the list.
print(animals[3])
# Print the sixth through tenth element of the list.
print(animals[6:10])
# Change the value of the seventh element to “onion”.
animals[6] = "Onion"
print(animals)
    # End Code