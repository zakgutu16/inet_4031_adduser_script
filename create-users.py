#!/usr/bin/python3

# Import necessary libraries
import os  # Allows Python to run operating system commands
import re  # Regular expression library for pattern matching
import sys  # Used to access standard input (input from the user)

# Read each line of input from the create-users.input file
for line in sys.stdin:
    # Check if the line is a comment (starts with #) and skip it
    match = re.match(r'^#', line)
    if match:
        continue

    # Split the line into fields based on the colon delimiter
    fields = line.strip().split(":")
    
    # If there are not enough fields, skip this line
    if len(fields) < 5:
        continue

    # Assign each field to a variable
    username = fields[0]
    password = fields[1]
    lastname = fields[2]
    firstname = fields[3]
    groups = fields[4]

    # Print the username being added
    print(f"Adding user: {username}")
    
    # Command to create the user without an initial password and with full name info
    cmd = f"sudo adduser --disabled-password --gecos \"{firstname} {lastname},,,\" {username}"
    # os.system(cmd)  # Uncomment this line when ready to actually add users

    # Command to set the user's password
    cmd = f"echo \"{username}:{password}\" | sudo chpasswd"
    # os.system(cmd)  # Uncomment this line when ready to actually set passwords

    # If the user has groups to join
    if groups != "-":
        grouplist = groups.split(",")  # Split multiple groups by comma
        for group in grouplist:
            # Command to add the user to each group
            cmd = f"sudo adduser {username} {group}"
            # os.system(cmd)  # Uncomment this line when ready to actually add users to groups

