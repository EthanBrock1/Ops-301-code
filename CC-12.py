#!/usr/bin/env python3

# Script: Ops 301 Class 12 Ops Challenge Solution
# Author:Ethan Brock
# Date of latest revision: 28MAR2023
# Purpose: 

    #REQUIREMENTS
# Prompt the user to type a string input as the variable for your destination
# URL.

# Prompt the user to select a HTTP Method of the following options:

# GET
# POST
# PUT
# DELETE
# HEAD
# PATCH
# OPTIONS
# Print to the screen the entire request your script is about to send.
# Ask the user to confirm before proceeding.

# Using the requests library, perform a GET request against your lab web server.

# For the given header, translate the codes into plain terms that print to the
# screen; for example, a 404 error should print Site not found to the terminal
# instead of 404.

# For the given URL, print response header information to the screen.

    #DEMO
# First you'll need to install the requests library to your system
# Next, like any library, import it into your Python script
    # import requests

# Assign a requests.get function to a variable. Be sure to pass a parameter 
# (the URL) into the function for it to work.
    # response = requests.get('https://api.github.com')

# Print the status code obtained by the function using [var name].status code
    # print(response.status_code)

# This will return status code 200. Look it up at
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

    # Start Code
import requests

# Prompt the user to type a string input as the variable for your destination
# URL.
http = input("Please enter the destination URL.")

# Prompt the user to select a HTTP Method
method = ["GET", "POST", "PUT", "DELETE", "HEAD", "PATCH", "OPTIONS"]



    # End Code