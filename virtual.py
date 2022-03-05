#! /usr/bin/python3

import subprocess


def main():
  subprocess.call('source ./venv/bin/activate', shell=True)
  subprocess.call('python tests.py', shell=True)
  subprocess.call('deactivate', shell=True)

if __name__ == "__main__":
  main()