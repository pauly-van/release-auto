#! /usr/bin/python3

import subprocess, os, json, sys, re
from tkinter import W

#comment out for testing, uncomment when everything functioning
#subprocess.call("yts discover", shell=True)


def id():
    with open('/Users/paulnguyen/Library/Preferences/yts_server/devices.json', 'r') as file:
        data = json.load(file)
        if data == []:
            raise ValueError('No devices were found to test CLI commands')
        return data[0]['shortId']

ID = id()

#Version
def yts_version():
    os.chdir('/Users/paulnguyen')
    os.system("curl -O -L https://dev.yts.devicecertification.youtube/yts_server.zip; rm -rf yts_server; unzip yts_server.zip -d yts_server")
    cliVer = subprocess.check_output("yts --version", shell=True)
    actual = subprocess.check_output(
        "curl http://dev.yts.devicecertification.youtube/version", shell=True)
    return cliVer.decode('UTF-8')[4:len(cliVer) -1], actual.decode('UTF-8')[0:]

#Discover
def yts_discover():
    discover = subprocess.run(["yts", "discover"], capture_output=True)
    output = re.search(r"\(\w\w\w?\)", discover.stdout.decode())
    return output != None

def yts_discover_return_options():
    discover = subprocess.run(["yts", "discover", "--verbose", "--colors", "--timeout=5"], capture_output=True)
    return discover.returncode

#Launch
def yts_launch():
    launch = subprocess.run(["yts", "launch", f"{ID}", "'https://www.youtube.com/tv?v=9szn1QQfas'"], capture_output=True)
    output = re.search(r"Launch request sent", launch.stdout.decode())
    return output != None

def yts_launch_returncode_options():
    launch = subprocess.run(["yts", "launch", f"{ID}", "'https://www.youtube.com/tv?v=9szn1QQfas'", "--verbose", "colors"], capture_output=True)
    return launch.returncode

#Stop
def yts_stop():
    subprocess.call(f"yts launch {ID} ''", shell=True)
    stop = subprocess.run(["yts", "stop", f"{ID}"], capture_output=True)
    output = re.search(r"Stop request sent", stop.stdout.decode())
    return output != None

def yts_stop_returncode_options():
    launch = subprocess.run(["yts", "launch", f"{ID}", "--verbose", "colors"], capture_output=True)
    return launch.returncode

#Test
def yts_test():
    test = subprocess.run(["yts", "test", f"{ID}", "'DOM CSS Tests CSS Media Rule CSSMediaRule.cssRules'"], capture_output=True)
    output = re.search(r"Executed 1 of 1 test", test.stdout.decode()) 
    return output != None
    
def yts_test_returncode_options():
    # need to add all other options (--module, --filter, --skip, --ports, --year, --program, --no-cap, --verticals)
    os.chdir("/home/doughfactory/")
    test = subprocess.run(["yts", "test", f"{ID}", "--verbose", "--colors", "--retry-failed=2", "--json-output='test.json'"], capture_output=True)
    return test.returncode

#List
def yts_list():
    list = subprocess.run(["yts", "list"], capture_output=True)
    output = re.search(r"Listed.*tests(s)", list.stdout.decode())
    return output != None

def yts_list_returncode_options():
    # need to add all other options (--module, --filter, --skip, --ports, --year, --program, --no-cap, --verticals)
    os.chdir("/home/doughfactory/")
    list = subprocess.run(["yts", "test", f"{ID}", "--verbose", "--colors", "--retry-failed=2", "--json-output='list_test.json'"], capture_output=True)
    return list.returncode

def yts_list_num():
    list = subprocess.run(["yts", "test", f"{ID}"], capture_output=True)
    output = re.search(r"1350", list.stdout.decode())
    return output != None

#Cert
def yts_cert():
    # need to add all other options (--module, --filter, --skip, --ports, --year, --program, --no-cap, --verticals)
    cert = subprocess.run(["yts", "cert", f"{ID}", "'DOM CSS Tests CSS Rule List CSSRuleList.item'", "--rerun"], capture_output=True)
    output = re.search(r"Executed", cert.stdout.decode())
    return output != None

def yts_list_returncode_options():
    # need to add all other options (--test-version, --filter, --skip, --ports, --upload/submit, --program, --no-cap, --verticals)
    os.chdir("/home/doughfactory/")
    list = subprocess.run(["yts", "test", f"{ID}", "--verbose", "--retry-failed=2", "--json-output='cert_test.json'"], capture_output=True)
    return list.returncode

#Login/User
def yts_login():
    pass

def yts_user():
    user = subprocess.run(["yts", "user"], capture_output=True)
    return user.returncode

#Credits
def yts_credits():
    credit = subprocess.run(["yts", "credits"], capture_output=True)
    output = re.search(r"https://www.npmjs.com/*", credit.stdout.decode())
    return output != None

def yts_credits_returncode_options():
    list = subprocess.run(["yts", "credits"], capture_output=True)
    return list.returncode

#Update
def yts_update():
    current_version = subprocess.check_output('yts --version', shell=True)
    subprocess.call('yts update', shell=True)
    # this will revert back to prod version
    updated_version = subprocess.check_output('yts --version', shell=True)
    return (current_version, updated_version)

#Evergreen
def yts_evergreen_channel_and_update():
    pass
