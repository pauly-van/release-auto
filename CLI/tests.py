#! /usr/bin/python3

import subprocess, os, json

subprocess.call("yts discover", shell=True)

def id():
  with open('/home/pauly/.local/share/yts_server/devices.json', 'r') as file:
    data = json.load(file)
    if data == []:
      raise ValueError('No devices were found to test CLI commands')
    return data[0]['shortId']
  
def ytsVersion():
  os.chdir('/home/pauly') 
  os.system("curl -O -L https://dev.yts.devicecertification.youtube/yts_server.zip; rm -rf yts_server; unzip yts_server.zip -d yts_server")
  cliVer = subprocess.check_output("yts --version", shell=True)
  actual = subprocess.check_output("curl http://dev.yts.devicecertification.youtube/version", shell=True)
  return cliVer.decode('UTF-8')[4:len(cliVer)-1], actual.decode('UTF-8')[0:]

def ytsDiscover():
  devices = subprocess.check_output("yts discover", shell=True)
  return devices.decode('UTF-8')[:21]

def ytsLaunch():
  output = subprocess.check_output("yts launch %s 'https://www.youtube.com/tv?v=9szn1QQfas'" % (id()), shell=True)  
  return output.decode('UTF-8')[0:19]

def ytsStop():
  ID = id()
  subprocess.call("yts launch %s ''" % (ID), shell=True)
  output = subprocess.check_output("yts stop %s" % (ID), shell=True)
  return output.decode('UTF-8')[0:17]

def ytsTest():
  ID = id()
  output = subprocess.check_output("yts test %s 'DOM CSS Tests'" % (ID), shell=True)
  print(output.decode('UTF-8'))

