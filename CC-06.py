#!/usr/bin/env python3

# Script: Ops 301 Class 06 Ops Challenge Solution
# Author:Ethan Brock
# Date of latest revision: 20MAR2023
# Purpose: Run bash commands whoami, ip a, and lshw -short.

# Requirements:

# The Python module "os" must be utilized
# At least three variables must be declared in Python that contain results of
# bash operations
# The Python function print() must be used at least three times
# Include execution of the following bash commands inside your Python script:

# whoami
# ip a
# lshw -short

# DEMO

    # How to use Linux/Bash commands within Python
    # First import the os library
        # import os

    # Then use os.system to call any kind of bash command
        # os.system("ls")

    # Here are some Python-specific operations for you to practice
    # How to print to terminal
        # print("Welcome to Python!")

    # How to declare a variable
        # var_greeting = "Welcome to Python!"

    # How to call a variable
        # print(var_greeting)

# Main


    # VARIABLES
who_ami = "Results for (whoami):"
ip_a = "Results for (ip a):"
ls_hw = "Results for (lshw -short)"

# Import the os library
import os

# Print results:

    # whoami

print(who_ami)
os.system("whoami")

    # ip a

print(ip_a)
os.system("ip a")

    # lshw -short

print(ls_hw)
os.system("lshw -short")

#End
