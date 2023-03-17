#!/bin/bash

# Script: Ops 301 Class 05 Ops Challenge Solution
# Author:Ethan Brock
# Date of latest revision: 17MAR2023
# Purpose: Clear Log files

#Variables
log1=/var/log/syslog
log2=/var/log/wtmp
stat1=$(stat -c%s "$log1")
stat2=$(stat -c%s "$log2")


# Main

# Print to the screen the file size of the log files before compression

echo "Size of $log1 = $stat1 bytes."
echo "Size of $log2 = $stat2 bytes."

# Compress the contents of the log files listed below to a backup directory
# /var/log/syslog
# /var/log/wtmp
# The file name should contain a time stamp with the following
# format -YYYYMMDDHHMMSS --- added with $(date +"-%y%m%d%H%M%S")
# Example: /var/log/backups/syslog-20220928081457.zip
    # --- added with $(date +"-%y%m%d%H%M%S")

tar -czf backup-$(date +"-%y%m%d%H%M%S").tar.gz "$log1" "$log2" 

# Clear the contents of the log file

sudo truncate -s 0 "$log1" "$log2"


# Print to screen the file size of the compressed file

bckup=$(stat -c%s backup-*.tar.gz)
echo "The new compressed file size is: $bckup bytes."

# Compare the size of the compressed files to the size of the original log files

echo "Original size of $log1 = $stat1 bytes."
echo "Original size of $log2 = $stat2 bytes."
echo "New compressed file size: $bckup bytes."

# End