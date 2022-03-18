#! /usr/bin/python3

import pytest, subprocess
from pathlib import Path
import tests

def test_cliVersion():
  versions = tests.ytsVersion()
  assert versions[0] == versions[1]

def test_cliDiscover():
  path = Path('/home/pauly/.local/share/yts_server/devices.json')
  assert tests.ytsDiscover() == 'Searching for devices' and path.is_file()

def test_cliLaunch():
  assert tests.ytsLaunch() == 'Launch request sent'

def test_cliStop():
  assert tests.ytsStop() == 'Stop request sent'