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

# ChatGPT was used to help. especially in figureing out how to link everything
    # Start Code

import requests

# Prompt user to enter a destination URL
url = input("Enter the URL: ")

# Prompt user to select HTTP method
method = input("Select an HTTP method (GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS): ")

# Print the entire request that will be sent
print(f"Sending {method} request to {url}")

# Confirm with user before proceeding
confirm = input("Do you want to proceed? (y/n): ")

if confirm.lower() == 'y':
    # Make the request using requests library
    response = requests.request(method, url)

    # Print the status code and reason phrase
    print(f"Status Code: {response.status_code} - {response.reason}")

    # Translate code to plain text
    if response.status_code == 200:
        status_text = "OK"
    elif response.status_code == 201:
        status_text = "Created"
    elif response.status_code == 204:
        status_text = "No Content"
    elif response.status_code == 304:
        status_text = "Not Modified"
    elif response.status_code == 400:
        status_text = "Bad Request"
    elif response.status_code == 401:
        status_text = "Unauthorized"
    elif response.status_code == 403:
        status_text = "Forbidden"
    elif response.status_code == 404:
        status_text = "Not Found"
    elif response.status_code == 409:
        status_text = "Request Conflict"
    elif response.status_code == 410:
        status_text = "URI no longer exists and has been permanently removed"
    elif response.status_code == 500:
        status_text = "Internal Server Error"
    else:
        status_text = "Unknown Error"

    print(f"Status: {status_text}")

    # Print the response headers
    print("\nResponse Headers:")
    for header, value in response.headers.items():
        print(f"{header}: {value}")

else:
    print("Request cancelled.")


    # End Code