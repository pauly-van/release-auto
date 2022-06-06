#! /usr/bin/python3

import subprocess
import os
import json

#comment out for testing, uncomment when everything functioning
#subprocess.call("yts discover", shell=True)


def id():
    with open('/Users/paulnguyen/Library/Preferences/yts_server/devices.json', 'r') as file:
        data = json.load(file)
        if data == []:
            raise ValueError('No devices were found to test CLI commands')
        return data[0]['shortId']


ID = id()


def yts_version():
    os.chdir('/Users/paulnguyen')
    os.system("curl -O -L https://dev.yts.devicecertification.youtube/yts_server.zip; rm -rf yts_server; unzip yts_server.zip -d yts_server")
    cliVer = subprocess.check_output("yts --version", shell=True)
    actual = subprocess.check_output(
        "curl http://dev.yts.devicecertification.youtube/version", shell=True)
    return cliVer.decode('UTF-8')[4:len(cliVer) -1], actual.decode('UTF-8')[0:]


def yts_discover():
    devices = subprocess.check_output("yts discover", shell=True)
    return devices.decode('UTF-8')[:21]


def yts_launch():
    output = subprocess.check_output(
        f"yts launch {ID} 'https://www.youtube.com/tv?v=9szn1QQfas'", shell=True)
    return output.decode('UTF-8')[0:19]


def yts_stop():
    subprocess.call(f"yts launch {ID} ''", shell=True)
    output = subprocess.check_output(f"yts stop {ID}", shell=True)
    return output.decode('UTF-8')[0:17]


def yts_test():
    output = subprocess.check_output(
        f"yts test {ID} 'DOM CSS Tests CSS Media Rule CSSMediaRule.cssRules'",
        shell=True)
    return output.decode('UTF-8')[len(output) - 51:len(output) - 31]


def yts_list():
    output = subprocess.check_output("yts list", shell=True)
    return output.decode("UTF-8")[len(output) - 21:len(output) - 1]


def yts_cert():
    output = subprocess.check_output(
        f"yts cert {ID} 'DOM CSS Tests CSS Rule List CSSRuleList.item' --rerun",
        shell=True)
    return output.decode("UTF-8")[len(output) - 45:len(output) - 19]


def yts_login():
    pass


def yts_user():
    pass


def yts_credits():
    pass


def yts_update():
    current_version = subprocess.check_output('yts --version', shell=True)
    subprocess.call('yts update', shell=True)
    # this will revert back to prod version
    updated_version = subprocess.check_output('yts --version', shell=True)
    return (current_version, updated_version)


def yts_evergreen_channel_and_update():
    pass
