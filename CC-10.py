#!/usr/bin/env python3

# Script: Ops 301 Class 10 Ops Challenge Solution
# Author:Ethan Brock
# Date of latest revision: 24MAR2023
# Purpose: Handle files in Python

    #REQUIREMENTS
# Using file handling commands, create a Python script that creates a new 
#.txt file, appends three lines, prints to the screen the first line, then
# deletes the .txt file.
    #DEMO

# Create a new file if it does not exist
    # f = open("demofile.txt", "w")

# How to open a file
    # f = open("demofile.txt")

# How to open a file and read it
    # f = open("demofile.txt", "r")
    #    print(f.read())

# How to return the five first characters of a file
    # f = open("demofile.txt", "r")
    # print(f.read(5))

# Close a file when you're finished
    # f = open("demofile.txt", "r")
    # print(f.readline())

    # Start Code
import os

# Create a new file if it does not exist
f = open("lab10.txt", "w")

# Appends three lines

with open('lab10.txt', 'w') as file:
   l1 = "The purpose of this script is to write multiple lines, view code for more detail \n"
   l2= "Done successfully\n"
   l3 = "Thank You!"
   file.writelines([l1, l2, l3])

# Print first line of .txt
with open('lab10.txt', 'r') as fp:
    first_item = fp.readline().strip()
print(first_item)

# Delete file

os.remove("lab10.txt")


    # End Code