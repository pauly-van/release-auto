#! /usr/bin/python3

import subprocess

def ytsDiscover():
  devices = subprocess.check_output("yts discover", shell=True)
  return devices.decode('UTF-8')[:21]

