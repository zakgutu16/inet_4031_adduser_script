#!/usr/bin/python3

# This script adds multiple users to the system based on an input file.
# It supports "dry-run" mode, allowing the user to preview the actions without making changes.
# If the user selects "Y" for dry-run, the script will only print the commands it would run.
# If the user selects "N", the script will actually run the commands and create users and groups.

import os
import re
import sys

# Prompt user for dry run mode
dry_run = input("Dry run? (Y/N): ").strip().lower()

for line in sys.stdin:
    match = re.match(r'^#', line)
    if match:
        if dry_run == 'y':
            print(f"Skipping line (commented out): {line.strip()}")
        continue

    fields = line.strip().split(":")
    if len(fields) < 5:
        if dry_run == 'y':
            print(f"Skipping line (not enough fields): {line.strip()}")
        continue

    username = fields[0]
    password = fields[1]
    lastname = fields[2]
    firstname = fields[3]
    groups = fields[4]

    print(f"Adding user: {username}")
    cmd = f"sudo adduser --disabled-password --gecos \"{firstname} {lastname},,,\" {username}"
    if dry_run == 'y':
        print(f"[DRY RUN] Would run: {cmd}")
    else:
        os.system(cmd)

    cmd = f"echo \"{username}:{password}\" | sudo chpasswd"
    if dry_run == 'y':
        print(f"[DRY RUN] Would run: {cmd}")
    else:
        os.system(cmd)

    if groups != "-":
        grouplist = groups.split(",")
        for group in grouplist:
            cmd = f"sudo adduser {username} {group}"
            if dry_run == 'y':
                print(f"[DRY RUN] Would run: {cmd}")
            else:
                os.system(cmd)

