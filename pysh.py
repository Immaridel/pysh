#!/usr/bin/python3

import sys
import paramiko

if len(sys.argv) < 2:
	print("args missing")
	sys.exit(1)

hostname = sys.argv[1]
cmd = sys.argv[2]

username = "immaridel"
password = "N0vember!1874"
port = "22"

client=paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname,port,username,password)
output=""
stdin, stdout, stderr = client.exec_command(cmd)

#print("ssh succuessful. Closing connection")
stdout=stdout.readlines()
client.close()
#print("Connection closed")

#print(stdout)
#print(cmd)
for line in stdout:
	output=output+line
if output!="":
	print(output)
else:
	print("There was no output for this command")
