#!/usr/local/bin/python3

import subprocess
from subprocess import * 
import datetime
import socket

pri = socket.gethostbyname(socket.gethostname())

pub = subprocess.check_output(['curl', '-s', 'ipecho.net/plain'])
public = pub.decode('utf-8')

print("Private IP: " + str(pri))

print("Public IP: " + str(public))

