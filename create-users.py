#!/usr/bin/python3

import os
import re
import sys

for line in sys.stdin:
    match = re.match(r'^#', line)
    if match:
        continue
    fields = line.strip().split(":")
    if len(fields) < 5:
        continue
    username = fields[0]
    password = fields[1]
    lastname = fields[2]
    firstname = fields[3]
    groups = fields[4]

    print(f"Adding user: {username}")
    cmd = f"sudo adduser --disabled-password --gecos \"{firstname} {lastname},,,\" {username}"
    # os.system(cmd)
    cmd = f"echo \"{username}:{password}\" | sudo chpasswd"
    # os.system(cmd)
    if groups != "-":
        grouplist = groups.split(",")
        for group in grouplist:
            cmd = f"sudo adduser {username} {group}"
            # os.system(cmd)

