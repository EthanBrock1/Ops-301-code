#!/usr/bin/env python3

# Script: Ops 301 Class 11 Ops Challenge Solution
# Author:Ethan Brock
# Date of latest revision: 27MAR2023
# Purpose: Fetch Info from Psutil

    #REQUIREMENTS
# Install Psutil.

# Create a Python script that fetches this information using Psutil:

# Time spent by normal processes executing in user mode
# Time spent by processes executing in kernel mode
# Time when system was idle
# Time spent by priority processes executing in user mode
# Time spent waiting for I/O to complete.
# Time spent for servicing hardware interrupts
# Time spent for servicing software interrupts
# Time spent by other operating systems running in a virtualized environment
# Time spent running a virtual CPU for guest operating systems under the control
# of the Linux kernel

    #DEMO
#!/usr/bin/env python3

# Libraries are imported at the top of any Python script using syntax import [library]
    # sudo pip install psutil

# Generate CPU times as a named tuple
    # print(psutil.cpu_times())

# Show current CPU consumption
        # print(psutil.cpu_percent())

    # Start Code
import psutil

# Get system CPU times
cpu_times = psutil.cpu_times()

# Time spent by normal processes executing in user mode
print("Time spent by normal processes executing in user mode:")
print(cpu_times.user)

# Time spent by processes executing in kernel mode
print("Time spent by processes executing in kernel mode:")
print(cpu_times.system)

# Time when system was idle
print("Time when system was idle:")
print(cpu_times.idle)

# Time spent by priority processes executing in user mode
print("Time spent by priority processes executing in user mode:")
print(cpu_times.nice)

# Time spent waiting for I/O to complete.
print("Time spent waiting for I/O to complete:")
print(cpu_times.iowait)

# Time spent for servicing hardware interrupts
print("Time spent for servicing hardware interrupts:")
print(cpu_times.irq)

# Time spent for servicing software interrupts
print("Time spent for servicing software interrupts:")
print(cpu_times.softirq)

# Time spent by other operating systems running in a virtualized environment
print("Time spent by other operating systems running in a virtualized environment:")
print(cpu_times.steal)

# Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel
print("Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel:")
print(cpu_times.guest)

    # End Code