#!/bin/bash

# Script: Ops 301 Class 03 Ops Challenge Solution
# Author:Ethan Brock
# Date of latest revision: 15MAR2023
# Purpose: 

# Main

# Prompts user for input directory path.

echo "Enter Directory path"
read dirpat

# Prompts user for input permissions number (e.g. 777 to perform a chmod 777)

echo "Enter Permissions number. (e.g. 777 to perform a chmod 777)"
read chmd

# Navigates to the directory input by the user and changes all files inside it
# to the input setting.
cd "$dirpat"
chmod -R "$chmd" .

# Prints to the screen the directory contents and the new permissions settings 
# of everything in the directory.

echo "New permissions settings for files in $dirpat:"
ls -la "$dirpat"