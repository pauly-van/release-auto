#! /usr/bin/python3

import pytest
from pathlib import Path
import tests


def assert_discover():
  path = Path('/home/pauly/.local/share/yts_server/devices.json')
  assert tests.ytsDiscover() == 'Searching for devices' and path.is_file()


