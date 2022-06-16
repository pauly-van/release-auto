#! /usr/bin/python3

import unittest
import subprocess
from pathlib import Path
import tests


class TestCliCommands(unittest.TestCase):

    def test_version_cmd(self):
        versions = tests.yts_version()
        self.assertEqual(versions[0], versions[1])


    def test_discover_cmd(self):
        path = Path(
            '/Users/paulnguyen/Library/Preferences/yts_server/devices.json')
        self.assertEqual(
            tests.yts_discover(),
            'Searching for devices',
            "Discover command failed to search for devices") and path.is_file()


    def test_launch_cmd(self):
        self.assertEqual(
            tests.yts_launch(),
            'Launch request sent',
            "Lanch command did not execute successfully")

    def test_stop_cmd(self):
        self.assertEqual(
            tests.yts_stop(),
            'Stop request sent',
            "Stop command did not execute successfully")

    def test_test_cmd(self):
        self.assertEqual(
            tests.yts_test(),
            "Executed 1 of 1 test",
            "Test command did not execute")

    def test_list_cmd(self):
        self.assertEqual(
            tests.yts_list(),
            "Listed 1219 test(s).",
            "List command did not execute or wrong number of tests")

    def test_cert_cmd(self):
        self.assertEqual(
            tests.yts_cert(),
            "Executed 1 of 1 test SUCCESS.\n",
            "Cert command did not execute")

    def test_login_user_cmd(self):
        pass

    def test_credits_cmd(self):
        pass

    def test_update_cmd(self):
        versions = tests.yts_update()
        self.assertNotEqual(
            versions[0],
            versions[1],
            "Both versions are the same after update command")

    def test_evergreen_channel_cmd(self):
        pass


if __name__ == '__main__':
    unittest.main()
