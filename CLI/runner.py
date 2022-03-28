#! /usr/bin/python3

import pytest, subprocess
from pathlib import Path
import tests

def test_version_cmd():
  versions = tests.ytsVersion()
  assert versions[0] == versions[1]

def test_discover_cmd():
  path = Path('/Users/paulnguyen/Library/Preferences/yts_server/devices.json')
  assert tests.ytsDiscover() == 'Searching for devices' and path.is_file()

def test_launch_cmd():
  assert tests.ytsLaunch() == 'Launch request sent'

def test_stop_cmd():
  assert tests.ytsStop() == 'Stop request sent'

def test_test_cmd():
  assert tests.ytsTest() == "Executed 1 of 1 test SUCCESS." or "Executed 1 of 1 test (1 FAILED)."

def test_list_cmd():
  pass

def test_cert_cmd():
  pass

def test_login_user_cmd():
  pass

def test_credits_cmd():
  pass

def test_update_cmd():
  pass

def test_evergreen_channel_cmd():
  pass

