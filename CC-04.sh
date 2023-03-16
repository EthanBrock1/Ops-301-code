#!/bin/bash

# Script: Ops 301 Class 04 Ops Challenge Solution
# Author: Ethan Brock
# Date of latest revision: 16MAR2023
# Purpose: 


# Create a bash script that launches a menu system with the following options:
# Hello world (prints “Hello world!” to the screen)
# Ping self (pings this computer’s loopback address)
# IP info (print the network adapter information for this computer)
# Exit

# Next, the user input should be requested.
# The program should next use a conditional statement to evaluate the user’s input, then act according to what the user selected.
# Use a loop to bring up the menu again after the request has been executed.

# Main
while true; do
    # Display the menu options
    echo "Menu Options:"
    echo "1. Hello World"
    echo "2. Ping Self"
    echo "3. IP Info"
    echo "4. Exit"

    # Prompt the user for input

    echo "Please select an option:"
    read input 
    

    # Evaluate the user's input using a conditional statement
    if [[ "$input" == "1" ]]; then
        # Print "Hello world!" to the screen
        echo "Hello world!"
    elif [[ "$input" == "2" ]]; then
        # Ping the loopback address
        ping 127.0.0.1
    elif [[ "$input" == "3" ]]; then
        # Print the network adapter information for this computer
        ip a
    elif [[ "$input" == "4" ]]; then
        # Exit the loop 
        echo "Exiting..."
        break
    else
        #invalid input
        echo "Invalid choice"
    fi

done
