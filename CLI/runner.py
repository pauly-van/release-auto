#! /usr/bin/python3

import pytest
import tests


def test_discover():
  assert tests.ytsDiscover() == 'Searching for devices', "Discover Utility searches"


def test_num():
  x=2
  assert x==2

