#! /usr/bin/python3

import unittest, subprocess, os
import tests

class TestCliTestCmd(unittest.TestCase):
    def test_version_cmd(self):
        versions = tests.yts_version()
        self.assertEqual(versions[0], versions[1])

class TestCliDiscoverCmd(unittest.TestCase):
    def test_discover_cmd(self):
        self.assertTrue(tests.yts_discover())

    def test_discover_returncode(self):
        self.assertIs(tests.yts_discover_return_options(), 0)

    def test_discover_creates_devices_file(self):
        self.assertTrue(os.path.isfile("/Users/kasatkina/Library/Preferences/yts_server/configs.json"))

class TestCliLaunchCmd(unittest.TestCase):
    def test_launch_cmd(self):
        self.assertTrue(tests.yts_launch())

    def test_launch_returncode(self):
        self.assertIs(tests.yts_launch_returncode_options(), 0)

class TestCliStopCmd(unittest.TestCase):
    def test_stop_cmd(self):
        self.assertTrue(tests.yts_stop())
    
    def test_stop_returncode(self):
        self.assertIs(tests.yts_stop_returncode_options(), 0)
        
class TestCliTestCmd(unittest.TestCase):
    def test_test_cmd(self):
        self.assertTrue(tests.yts_test())
    
    def test_test_returncode(self):
        self.assertIs(tests.yts_test_returncode_options(), 0)
    
    def test_test_json_output(self):
        self.assertTrue(os.path.isfile("/Users/kasatkina/test.json"))

class TestCliListCmd(unittest.TestCase):
    def test_list_cmd(self):
        self.assertTrue(tests.yts_list())

    def test_list_returncode_options(self):
        self.assertIs(tests.yts_list_returncode_options(), 0)

    def test_list_num_of_tests(self):
        self.assertTrue(tests.yts_list_num())

    def test_list_json_output(self):
        self.assertTrue(os.path.isfile("/Users/kasatkina/list_test.json"))

class TestCliCertCmd(unittest.TestCase):
    def test_cert_cmd(self):
        self.assertTrue(tests.yts_cert())
    
    def test_cert_returncode(self):
        self.assertIs(tests.yts_cert_returncode_options(), 0)

    def test_cert_json_output(self):
        self.assertTrue(os.path.isfile("/Users/kasatkina/cert_test.json"))
class TestCliLoginCmd(unittest.TestCase):
    #need to figure how to do this automated as it asks to continue login on browser
    def test_login_cmd(self):
        pass

class TestCliUserCmd(unittest.TestCase):
    def test_user_cmd(self):
        self.assertIs(tests.yts_user(), 0)

class TestCliCreditsCmd(unittest.TestCase):
    def test_credits_cmd(self):
        self.assertTrue(tests.yts_credits())
    
    def test_credit_returncode(self):
        self.assertIs(tests.yts_cert_returncode_options(), 0)

class TestCliUpdateCmd(unittest.TestCase):
    def test_update_cmd(self):
        versions = tests.yts_update()
        self.assertNotEqual(
            versions[0],
            versions[1],
            "Both versions are the same after update command")

class TestCliEvergreenChannelCmd(unittest.TestCase):
    def test_evergreen_channel_cmd(self):
        pass

if __name__ == '__main__':
    unittest.main()
