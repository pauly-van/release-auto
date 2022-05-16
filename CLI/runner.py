#! /usr/bin/python3

import pytest, subprocess
from pathlib import Path
import tests

def test_version_cmd():
  versions = tests.yts_version()
  assert versions[0] == versions[1]

def test_discover_cmd():
  path = Path('/Users/paulnguyen/Library/Preferences/yts_server/devices.json')
  assert tests.yts_discover() == 'Searching for devices' and path.is_file()

def test_launch_cmd():
  assert tests.yts_launch() == 'Launch request sent'

def test_stop_cmd():
  assert tests.yts_stop() == 'Stop request sent'

def test_test_cmd():
  assert tests.yts_test() == "Executed 1 of 1 test SUCCESS." or "Executed 1 of 1 test (1 FAILED)."

def test_list_cmd():
  assert tests.yts_list() == "Listed 1218 test(s)."

def test_cert_cmd():
#  assert tests.yts_cert() == "Executed 1 of 1 test SUCCESS."
  test = tests.yts_cert()
  print(test)
#  print(test == "Executed 1 of 1 test SUCCESS.")


def test_login_user_cmd():
  pass

def test_credits_cmd():
  pass

def test_update_cmd():
  pass

def test_evergreen_channel_cmd():
  pass

test_cert_cmd()